# Generated by Django 3.2.5 on 2022-01-22 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0031_teammember'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='Duolingo',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='students',
            name='PTE',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='students',
            name='TOEFL',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
    ]
