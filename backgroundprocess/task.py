from celery.task.schedules import crontab
from celery.decorators import periodic_task
from celery.utils.log import get_task_logger

# from merger.Task import add_to_db

logger = get_task_logger(__name__)


@periodic_task(
    run_every=(crontab(minute='*/15')),
    name="task_merge_data",
    ignore_result=True
)
def task_merge_data():
    """
    Merges data created and adds a final data points
    """
    data_to_db()
    logger.info("Data Merged")
