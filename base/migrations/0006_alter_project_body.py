# Generated by Django 4.0.5 on 2022-06-22 09:00

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_alter_project_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='body',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]