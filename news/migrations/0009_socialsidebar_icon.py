# Generated by Django 4.0.4 on 2022-05-07 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0008_socialsidebar_social_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='socialsidebar',
            name='icon',
            field=models.ImageField(blank=True, null=True, upload_to='news/'),
        ),
    ]