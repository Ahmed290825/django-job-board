# Generated by Django 3.1.1 on 2020-09-11 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Job', '0004_auto_20200911_1004'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
        ),
    ]
