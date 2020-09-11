# Generated by Django 3.1.1 on 2020-09-11 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Job', '0003_job_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='experince',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='job',
            name='published_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='job',
            name='salary',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='job',
            name='vacancy',
            field=models.IntegerField(default=1),
        ),
    ]
