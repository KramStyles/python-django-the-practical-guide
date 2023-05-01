from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.

class Review(models.Model):
    username = models.CharField(max_length=100)
    ratings = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    review = models.TextField(verbose_name="Your Review")
