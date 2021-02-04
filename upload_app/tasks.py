from celery import shared_task
from .models import *

@shared_task()
def delete_file(date):
    deleted_task = CreateFiles.objects.get(create_date__in=date)
    print(deleted_task)
    deleted_task.delete()
    return 'Success'
