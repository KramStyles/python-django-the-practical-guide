# Generated by Django 4.2 on 2023-04-22 17:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("book", "0004_author_alter_book_is_bestselling_alter_book_slug_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Address",
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
                ("street", models.CharField(max_length=80)),
                ("postal_code", models.CharField(max_length=10)),
                ("city", models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name="book",
            name="author",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="books",
                to="book.author",
            ),
        ),
        migrations.AddField(
            model_name="author",
            name="address",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="book.address",
            ),
        ),
    ]
