# Generated by Django 4.0.5 on 2022-07-05 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0016_alter_skill_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='logo',
            field=models.ImageField(default='skillLogo.png', null=True, upload_to=''),
        ),
    ]