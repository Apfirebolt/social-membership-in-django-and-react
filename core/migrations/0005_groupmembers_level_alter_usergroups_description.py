# Generated by Django 4.2.7 on 2023-11-28 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0004_groupmembers_delete_usergroupmapping"),
    ]

    operations = [
        migrations.AddField(
            model_name="groupmembers",
            name="level",
            field=models.CharField(
                blank=True, max_length=255, null=True, verbose_name="Level"
            ),
        ),
        migrations.AlterField(
            model_name="usergroups",
            name="description",
            field=models.TextField(
                blank=True, null=True, verbose_name="Group Description"
            ),
        ),
    ]
