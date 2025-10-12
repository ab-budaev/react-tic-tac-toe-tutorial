import time
from typing import Final

from celery_app import app


# Per-task limits ensure timeout even if global config changes
@app.task(bind=True, name="tasks.long_running_timeout", soft_time_limit=3, time_limit=5)
def long_running_timeout(self, duration_seconds: int = 60) -> str:
    """Intentionally long task that will exceed Celery time limits."""
    time.sleep(duration_seconds)
    return "completed"
