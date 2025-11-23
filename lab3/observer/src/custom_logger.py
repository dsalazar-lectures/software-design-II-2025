"""
custom_logger.py
----------------
A tiny logging framework that demonstrates the Observer pattern using Python's
standard `logging` module. The Logger (Subject) publishes a record and multiple
Handlers (Observers) react: console, JSONL, CSV, and in-memory metrics.

Key points:
- Business logic is NOT coupled to output destinations. Adding/removing a
  destination is just adding/removing a Handler.
- The audit fields (user, role, action, description) are passed via `extra` and
  each handler reads them from the LogRecord.
"""

from __future__ import annotations
import csv
import json
import logging
from dataclasses import dataclass, asdict
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional


# -----------------------------------------------------------------------------
# 1) Event model
# -----------------------------------------------------------------------------
@dataclass
class AuditEvent:
    """
    Structure of audit data we expect for each log entry.
    It is converted to `extra` for the logger.
    """
    user: str
    role: str
    action: str
    description: str


# -----------------------------------------------------------------------------
# 2) Common helpers for timestamp + record extraction
# -----------------------------------------------------------------------------
def _timestamp_utc(record: logging.LogRecord) -> str:
    """UTC timestamp with Z suffix (ISO-like)."""
    return datetime.utcfromtimestamp(record.created).isoformat(timespec="seconds") + "Z"


def _event_dict(record: logging.LogRecord) -> Dict[str, Any]:
    """Converts a LogRecord into a uniform dict for handlers."""
    return {
        "timestamp": _timestamp_utc(record),
        "level": record.levelname,
        "logger": record.name,
        "user": getattr(record, "user", "-"),
        "role": getattr(record, "role", "-"),
        "action": getattr(record, "action", "-"),
        "description": getattr(record, "description", "-"),
    }


# -----------------------------------------------------------------------------
# 3) Handlers (Observers)
# -----------------------------------------------------------------------------
class JSONLinesHandler(logging.Handler):
    """
    Writes each record as a JSON line (JSONL). Good for later ingestion/analysis.
    """
    def __init__(self, path: str, level: int = logging.INFO):
        super().__init__(level)
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)

    def emit(self, record: logging.LogRecord) -> None:
        try:
            with self.path.open("a", encoding="utf-8") as f:
                f.write(json.dumps(_event_dict(record), ensure_ascii=False) + "\n")
        except Exception:
            self.handleError(record)


class CSVHandler(logging.Handler):
    """
    Writes CSV with header. Easy to open in spreadsheets.
    """
    HEADERS = ["timestamp", "level", "logger", "user", "role", "action", "description"]

    def __init__(self, path: str, level: int = logging.INFO):
        super().__init__(level)
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self._ensure_header()

    def _ensure_header(self) -> None:
        if not self.path.exists() or self.path.stat().st_size == 0:
            with self.path.open("w", newline="", encoding="utf-8") as f:
                csv.writer(f).writerow(self.HEADERS)

    def emit(self, record: logging.LogRecord) -> None:
        try:
            row = _event_dict(record)
            with self.path.open("a", newline="", encoding="utf-8") as f:
                csv.writer(f).writerow([row[h] for h in self.HEADERS])
        except Exception:
            self.handleError(record)


class MetricsHandler(logging.Handler):
    """
    Simple in-memory counter (key = "action|LEVEL").
    Useful for demos/quick validation. For real monitoring, export to Prometheus/Grafana.
    """
    def __init__(self, level: int = logging.INFO):
        super().__init__(level)
        self.counts: Dict[str, int] = {}

    def emit(self, record: logging.LogRecord) -> None:
        key = f"{getattr(record, 'action', 'unknown')}|{record.levelname}"
        self.counts[key] = self.counts.get(key, 0) + 1

    def snapshot(self) -> Dict[str, int]:
        """Returns a copy of the counters (for printing or testing)."""
        return dict(self.counts)

class PlainTextHandler(logging.Handler):
    """
    Writes each record as a single formatted text line into a .txt file.
    Uses a logging.Formatter so you can customize the line format if desired.
    """
    def __init__(
        self,
        path: str,
        level: int = logging.INFO,
        fmt: str | None = None,
        datefmt: str = "%Y-%m-%d %H:%M:%S",
    ):
        super().__init__(level)
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)

        # Default format mirrors the console output
        if fmt is None:
            fmt = "%(asctime)s | %(levelname)s | User:%(user)s | Role:%(role)s | Action:%(action)s | %(description)s"

        self.setFormatter(logging.Formatter(fmt=fmt, datefmt=datefmt))

    def emit(self, record: logging.LogRecord) -> None:
        try:
            line = self.format(record)  # uses the formatter above
            with self.path.open("a", encoding="utf-8") as f:
                f.write(line + "\n")
        except Exception:
            self.handleError(record)


# -----------------------------------------------------------------------------
# 4) Logger (Subject)
# -----------------------------------------------------------------------------
class CustomLogger:
    """
    Facade over the standard logger with:
      - pluggable handlers (console/JSONL/CSV/Metrics),
      - short methods: log/info/warning/error/debug.

    Typical usage:
        logger = CustomLogger("AuditLogger", handlers=build_default_handlers())
        logger.info(user="u1", role="admin", action="create_user", description="OK")
    """

    def __init__(
        self,
        name: str = "AppLogger",
        handlers: Optional[Iterable[logging.Handler]] = None,
        level: int = logging.DEBUG,
    ) -> None:
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        self.logger.propagate = False  # avoid duplicating to root

        # Default console handler
        if handlers is None:
            console_handler = logging.StreamHandler()
            console_handler.setLevel(logging.DEBUG)
            console_handler.setFormatter(logging.Formatter(
                fmt="%(asctime)s | %(levelname)s | User:%(user)s | Role:%(role)s | Action:%(action)s | %(description)s",
                datefmt="%Y-%m-%d %H:%M:%S",
            ))
            handlers = [console_handler]

        # Avoid duplicating handlers if several instances share the same logger name
        if not self.logger.handlers:
            for h in handlers:
                self.logger.addHandler(h)

    # -------- Main API --------------------------------------------------------
    def log(self, level: str, user: str, role: str, action: str, description: str) -> None:
        """
        Publishes an audit event with the given level.
        Valid levels: info, warning, error, debug.
        """
        event = AuditEvent(user=user, role=role, action=action, description=description)
        extra = asdict(event)

        method = {
            "info": self.logger.info,
            "warning": self.logger.warning,
            "error": self.logger.error,
            "debug": self.logger.debug,
        }.get(level.lower(), self.logger.info)

        method("", extra=extra)

    # -------- Shortcuts -------------------------------------------------------
    def info(self, **logargs: str) -> None:    self.log("info",    **logargs)   # type: ignore[arg-type]
    def warning(self, **logargs: str) -> None: self.log("warning", **logargs)   # type: ignore[arg-type]
    def error(self, **logargs: str) -> None:   self.log("error",   **logargs)   # type: ignore[arg-type]
    def debug(self, **logargs: str) -> None:   self.log("debug",   **logargs)   # type: ignore[arg-type]


# -----------------------------------------------------------------------------
# 5) Convenience builder for handlers
# -----------------------------------------------------------------------------
def build_default_handlers(out_dir: str = "lab3/observer/out") -> List[logging.Handler]:
    """
    Returns 4 handlers: console, JSONL, CSV and in-memory metrics.
    """
    Path(out_dir).mkdir(parents=True, exist_ok=True)

    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)
    console.setFormatter(logging.Formatter(
        fmt="%(asctime)s | %(levelname)s | User:%(user)s | Role:%(role)s | Action:%(action)s | %(description)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    ))

    jsonl = JSONLinesHandler(str(Path(out_dir) / "audit.jsonl"))
    csvh  = CSVHandler(str(Path(out_dir) / "audit.csv"))
    txt     = PlainTextHandler(str(Path(out_dir) / "audit.txt"))
    metrics = MetricsHandler()

    return [console, jsonl, csvh, txt, metrics]
