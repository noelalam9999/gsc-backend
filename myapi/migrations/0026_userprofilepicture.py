# Generated by Django 3.2.5 on 2022-01-05 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0025_agents_active_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfilePicture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='post_images')),
            ],
        ),
    ]