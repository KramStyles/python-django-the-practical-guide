# Generated by Django 4.2 on 2023-05-03 14:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0002_alter_post_tags"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="image_name",
            field=models.ImageField(upload_to="blog"),
        ),
    ]