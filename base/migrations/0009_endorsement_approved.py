# Generated by Django 4.0.5 on 2022-06-24 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_endorsement'),
    ]

    operations = [
        migrations.AddField(
            model_name='endorsement',
            name='approved',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
