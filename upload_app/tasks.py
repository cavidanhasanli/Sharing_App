from celery import shared_task
from upload_app.models import *
from django.utils import timezone
from datetime import datetime, timedelta


# delete_file(now)


@shared_task()
def delete_file():
    now = timezone.now() - timedelta(days=7)

    try:
        get_data = CreateFiles.objects.get(create_date=now)
        get_data.delete()
    except:
        None
        print('Error Message:not working this a function')
