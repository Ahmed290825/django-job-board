# Generated by Django 3.1.1 on 2020-09-11 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Job', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='job_type',
            field=models.CharField(choices=[('full time', 'full time'), ('part time', 'part time')], default='', max_length=15),
            preserve_default=False,
        ),
    ]
