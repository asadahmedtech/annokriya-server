from celery.task.schedules import crontab
from celery.decorators import periodic_task
from celery.utils.log import get_task_logger
from backend.celery import app
from merger.Task import add_to_db
from .models import TaskHistory
from datetime import datetime

logger = get_task_logger(__name__)


# @periodic_task(
#     run_every=(crontab(minute='*/2')),
#     name="task_merge_data",
#     ignore_result=True
# )
# @app.task(name = "task_merge_data")
# def task_merge_data():
#     """
#     Merges data created and adds a final data points
#     """
#     print("Merged")
#     data_to_db()
#     logger.info("Data Merged")


# from celery.task import tasks
# from celery.task import Task

# class task_merge_data(Task):
# 	def run():
# 		print("Merged")
#     	data_to_db()
#     	logger.info("Data Merged")

# app.tasks.register(task_merge_data())

from celery import task 
@task()
def task_merge_data():
    """
    Merges data created and adds a final data points
    """
    print("Merged")
    result = add_to_db()
    name = "merger"

    now = datetime.now()
    date_now = now.strftime("%d-%m-%Y %H:%M:%S")
    taskhistory = TaskHistory.objects.get_or_create(name=name)[0]
    taskhistory.history.update({date_now: "Merged", "Output" : result})
    taskhistory.save()
    logger.info("Data Merged")