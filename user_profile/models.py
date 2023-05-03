from django.db import models


class UserProfile(models.Model):
    cv = models.FileField(upload_to="user_profile", verbose_name="Curriculum Vitae")
    image = models.ImageField(upload_to="user_profile", verbose_name="Profile Picture")
