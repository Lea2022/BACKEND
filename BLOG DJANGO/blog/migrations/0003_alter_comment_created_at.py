# Generated by Django 5.1 on 2024-08-29 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_post_author_comment"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
