# Generated by Django 4.0.5 on 2022-06-21 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_alter_skill_body_alter_tag_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='thumbnail',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]