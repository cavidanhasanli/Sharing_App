# Generated by Django 3.1.6 on 2021-02-11 08:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import upload_app.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CreateFiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(blank=True, max_length=50, null=True)),
                ('my_file', models.FileField(blank=True, null=True, upload_to=upload_app.models.content_file_name)),
                ('file_description', models.CharField(blank=True, max_length=255, null=True)),
                ('create_date', models.DateField(auto_now_add=True, null=True)),
                ('user_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SenderFiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sended_files', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='upload_app.createfiles')),
                ('sended_users', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_id', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(blank=True, null=True)),
                ('sender_file', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='upload_app.senderfiles')),
            ],
        ),
    ]
