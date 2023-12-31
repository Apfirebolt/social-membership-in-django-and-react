# Generated by Django 4.2.7 on 2023-11-25 10:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="UserGroups",
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
                ("name", models.CharField(max_length=255, verbose_name="Group Name")),
                (
                    "description",
                    models.TextField(blank=True, null=True, verbose_name="First Name"),
                ),
                (
                    "createdAt",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created At"),
                ),
                (
                    "createdBy",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="group_created_by",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Group",
            },
        ),
    ]
