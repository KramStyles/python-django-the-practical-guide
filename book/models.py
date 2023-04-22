from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.


class Country(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=3)

    class Meta:
        verbose_name_plural = "Countries"

    def __str__(self):
        return self.name


class Address(models.Model):
    street = models.CharField(max_length=80)
    postal_code = models.CharField(max_length=10)
    city = models.CharField(max_length=50)

    class Meta:
        """Metaclass to modify Address Model"""

        verbose_name_plural = "Address Entries"

    def __str__(self):
        return self.street


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    # Not adding related_name here because it's 1to1 and author is default
    address = models.OneToOneField(Address, models.PROTECT, null=True)

    def full_name(self):
        return f"{self.first_name} {self.last_name}".title()

    def __str__(self):
        return self.full_name()


class Book(models.Model):
    title = models.CharField(max_length=100)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    author = models.ForeignKey(
        Author,
        on_delete=models.PROTECT,
        null=True,
        related_name="books"
        # Added related name, so we can reverse relationship from author.
        #  E.g. rowling_books = Book.objects.filter(author__last_name="Rowling")
        # rowling_books => [Harry porter 1, Harry Porter 2]
        # ##
        # rowling = Author.objects.get(last_name = "Rowling")
        # rowling_books = rowling.books.all()
    )
    is_bestselling = models.BooleanField(default=False, verbose_name="Is Best-Seller?")

    # Adding editable = False would hide the field in the admin
    slug = models.SlugField(default="", blank=True, db_index=True)

    published_countries = models.ManyToManyField(Country, related_name="books")
    # To add use this example. book = Book.objects.first
    # germany = Country.object.get(code="DE")
    # book.published_countries.add(germany)

    def __str__(self):
        return f"{self.title} by {self.author}"

    def save(
        self,
        force_insert=False,
        force_update=False,
        using=None,
        update_fields=None,
        *args,
        **kwargs,
    ):
        # taking this out because of pre-population
        # self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("book-detail", args=[self.slug])
