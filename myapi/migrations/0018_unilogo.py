# Generated by Django 3.2.5 on 2021-12-12 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0017_agentcert'),
    ]

    operations = [
        migrations.CreateModel(
            name='UniLogo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='post_images')),
            ],
        ),
    ]