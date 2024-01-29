# Generated by Django 4.2.8 on 2024-01-28 06:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("courses", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Lecturer",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(verbose_name="Lecturer Name")),
                ("url", models.URLField(verbose_name="Lecturer Homepage URL")),
                (
                    "is_resigned",
                    models.BooleanField(default=False, verbose_name="The lecturer is resigned from the college"),
                ),
            ],
        ),
        migrations.AddField(
            model_name="course",
            name="course_exclusions",
            field=models.CharField(default="", verbose_name="Course Exclusions"),
            preserve_default=False,
        ),
    ]
