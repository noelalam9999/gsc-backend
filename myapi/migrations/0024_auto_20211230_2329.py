# Generated by Django 3.2.5 on 2021-12-30 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0023_agents_added_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='uni',
            name='Accomodation',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='uni',
            name='Internship',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='uni',
            name='OfferLetter',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='uni',
            name='WorkStudy',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='uni',
            name='WorkVisa',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
    ]