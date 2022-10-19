# Generated by Django 4.1.2 on 2022-10-19 15:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("Users", "0005_userprofile_is_staff"),
    ]

    operations = [
        migrations.CreateModel(
            name="ProfileFeedItem",
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
                ("status_text", models.CharField(max_length=255)),
                ("creted_on", models.DateTimeField(auto_now_add=True)),
                (
                    "user_profile",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]