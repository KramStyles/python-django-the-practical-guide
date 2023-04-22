from django.core.validators import MinLengthValidator
from django.db import models

from book.models import Author

# Create your models here.


class Tag(models.Model):
    caption = models.CharField(max_length=50)

    def __str__(self):
        return self.caption


class Post(models.Model):
    title = models.CharField(max_length=250)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name="posts")
    excerpt = models.CharField(max_length=150, blank=True)
    image_name = models.CharField(max_length=250)
    slug = models.SlugField(blank=True, unique=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    tags = models.ManyToManyField(Tag)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
