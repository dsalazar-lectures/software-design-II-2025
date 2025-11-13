"""
Minimal demonstration of CustomLogger.

Run:
    python lab3/observer/src/demo.py

Outputs:
    - Prints to console
    - Generates lab3/observer/out/audit.jsonl and audit.csv
    - Prints in-memory metrics
"""

from custom_logger import CustomLogger, build_default_handlers, MetricsHandler

# 1) Create logger with 4 observers (handlers)
logger = CustomLogger("AuditLogger", handlers=build_default_handlers())
# loggerRecipe = CustomLogger("RecipeLogger", PlainTextHandler())

# 2) Emit a few sample logs
logger.info(user="u-001", role="superadmin", action="create_user", description="Created demo user")
logger.warning(user="u-002", role="admin", action="ban_user", description="Temporary ban (24h)")
logger.error(user="u-003", role="user", action="delete_recipe", description="Insufficient permission")
logger.debug(user="u-004", role="analyst", action="search_recipe", description="Query 'tacos'")

# 3) Read metrics from the corresponding handler
metrics = next(h for h in logger.logger.handlers if isinstance(h, MetricsHandler))
print("\nMetrics (action|LEVEL => count):")
for k, v in metrics.snapshot().items():
    print(f"  {k}: {v}")
