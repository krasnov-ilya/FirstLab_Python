# Generated by Django 3.0.4 on 2020-03-30 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20200330_1444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='views',
            field=models.BigIntegerField(default=0),
        ),
    ]
