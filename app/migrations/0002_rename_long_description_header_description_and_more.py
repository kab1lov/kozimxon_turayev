# Generated by Django 4.2.7 on 2023-12-28 18:11

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="header",
            old_name="long_description",
            new_name="description",
        ),
        migrations.RemoveField(
            model_name="header",
            name="short_description",
        ),
    ]
