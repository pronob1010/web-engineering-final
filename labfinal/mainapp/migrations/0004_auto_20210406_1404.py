# Generated by Django 3.1.7 on 2021-04-06 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_auto_20210406_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
