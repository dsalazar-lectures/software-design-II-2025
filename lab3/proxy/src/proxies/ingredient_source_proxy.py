from typing import Callable, Optional


class IngredientSourceProxy:
    def __init__(self, real_or_factory: "Callable[[], object] | object"):
        self._factory: Optional[Callable[[], object]] = None
        self._real: Optional[object] = None
        if callable(real_or_factory):
            self._factory = real_or_factory
        else:
            self._real = real_or_factory
        self._cache: dict[str, Optional[str]] = {}

    def _ensure_real(self):
        if self._real is None and self._factory is not None:
            print("[Proxy] Creando fuente real (lazy)")
            self._real = self._factory()
        return self._real

    def get(self, name: str):
        key = name.lower()
        if key in self._cache:
            print(f"[Proxy] '{name}' -> CACHÉ")
            return self._cache[key]
        print(f"[Proxy] '{name}' -> REAL")
        real = self._ensure_real()
        value = real.get(name)
        self._cache[key] = value
        return value
