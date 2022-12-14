# Generated by Django 4.1.1 on 2022-09-25 12:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("server", "0003_project_client_project_heading"),
    ]

    operations = [
        migrations.CreateModel(
            name="ProjectImage",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                ("image", models.ImageField(upload_to="images")),
                (
                    "projectId",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="server.project"
                    ),
                ),
            ],
        ),
    ]
