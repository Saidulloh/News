# Generated by Django 4.0.4 on 2022-05-18 13:58

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0017_delete_addposts_alter_comment_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]