# Generated by Django 3.2.5 on 2022-03-22 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0041_remove_application_prev_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsletterCampaign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('campaign_name', models.CharField(max_length=60)),
                ('recipient_list', models.CharField(blank=True, max_length=60, null=True)),
                ('message', models.CharField(blank=True, max_length=60, null=True)),
                ('subj', models.CharField(blank=True, max_length=60, null=True)),
            ],
        ),
    ]
