# Generated by Django 3.2.5 on 2021-08-26 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0007_auto_20210822_2202'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='birth_date',
            field=models.CharField(default=23, max_length=60),
            preserve_default=False,
        ),
    ]
