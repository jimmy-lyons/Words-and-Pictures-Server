# Generated by Django 4.1.1 on 2022-09-23 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("server", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="description",
            field=models.TextField(default=""),
        ),
    ]
