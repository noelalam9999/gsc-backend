# Generated by Django 3.2.5 on 2022-03-30 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0045_auto_20220329_0916'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='extracurricular',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='students',
            name='parents_contact_number',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='students',
            name='parents_email',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='students',
            name='parents_name',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='students',
            name='parents_profession',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='students',
            name='prev_institution',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='students',
            name='work_experience',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
    ]