# Generated by Django 4.2.2 on 2023-06-30 08:08

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("todo", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="task",
            options={"ordering": ("is_done", "datetime")},
        ),
    ]
