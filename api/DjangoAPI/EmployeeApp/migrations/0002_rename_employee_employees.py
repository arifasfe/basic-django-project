# Generated by Django 4.2.6 on 2023-10-30 15:33

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("EmployeeApp", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Employee",
            new_name="Employees",
        ),
    ]
