# Generated by Django 3.2.5 on 2021-12-12 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0018_unilogo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('program_name', models.CharField(max_length=60)),
                ('duration', models.CharField(blank=True, max_length=60, null=True)),
                ('required_ielts', models.CharField(blank=True, max_length=60, null=True)),
                ('fee', models.CharField(blank=True, max_length=60, null=True)),
                ('department', models.CharField(blank=True, max_length=60, null=True)),
                ('partner', models.CharField(blank=True, max_length=60, null=True)),
            ],
        ),
    ]
