# Generated by Django 3.2.9 on 2021-11-27 15:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("web", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="mainblock",
            name="page_section",
        ),
        migrations.DeleteModel(
            name="Main",
        ),
        migrations.DeleteModel(
            name="MainBlock",
        ),
    ]
