from django.core.validators import MinLengthValidator
from django.db import models
from django.shortcuts import reverse

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
    image_name = models.ImageField(upload_to="blog")
    slug = models.SlugField(blank=True, unique=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    tags = models.ManyToManyField(Tag, related_name="tags")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog-post-details", args=[self.slug])

    def save(self, *args, **kwargs):
        self.excerpt = self.excerpt.replace("-", " ").capitalize()
        super().save(*args, **kwargs)


class Comment(models.Model):
    user_name = models.CharField(max_length=100)
    user_email = models.EmailField()
    text = models.TextField(verbose_name="Comment", max_length=500)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user_name}"
