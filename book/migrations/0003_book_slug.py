# Generated by Django 4.2 on 2023-04-22 10:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("book", "0002_book_author_book_is_bestselling_alter_book_rating"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="slug",
            field=models.SlugField(default=""),
        ),
    ]