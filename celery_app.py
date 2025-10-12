import os
from celery import Celery


def _env(name: str, default: str) -> str:
    return os.environ.get(name, default)


app = Celery(
    "timeout_demo",
    broker=_env("CELERY_BROKER_URL", "redis://localhost:6379/0"),
    backend=_env("CELERY_RESULT_BACKEND", "redis://localhost:6379/1"),
)

# Ensure the worker imports our tasks module
app.conf.update(
    imports=("tasks",),
    # Small limits so the demo task reliably times out
    task_time_limit=int(_env("CELERY_TASK_TIME_LIMIT", "5")),       # hard limit (seconds)
    task_soft_time_limit=int(_env("CELERY_TASK_SOFT_TIME_LIMIT", "3")),  # soft limit (seconds)
    timezone="UTC",
    enable_utc=True,
)
