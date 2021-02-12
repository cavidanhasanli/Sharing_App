import os

from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.

def content_file_name(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (instance.file_name, ext)
    return os.path.join('uploads', filename)


class CreateFiles(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    file_name = models.CharField(max_length=50, null=True, blank=True)
    my_file = models.FileField(upload_to=content_file_name, null=True, blank=True)
    file_description = models.CharField(max_length=255, null=True, blank=True)
    create_date = models.DateField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f'{self.file_name}'


class SenderFiles(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='user_id')
    sended_users = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    sended_files = models.ForeignKey(CreateFiles, on_delete=models.CASCADE, null=True, blank=True)
    comment_activate = models.BooleanField(default=False,null=True,blank=True)

    def __str__(self):
        return f'{self.sended_users} / {self.sended_files}'


class Comment(models.Model):
    sender_file = models.ForeignKey(SenderFiles, on_delete=models.CASCADE, null=True, blank=True)
    comment = models.TextField(null=True,blank=True)

    def __str__(self):
        return f'{self.sender_file} / {self.comment}'