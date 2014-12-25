from django.db import models


# Create your models here.
class Category(models.Model):
    english_name = models.CharField(max_length=255)
    arabic_name = models.CharField(max_length=255)


class Company(models.Model):
    name = models.CharField(max_length=255)
    short_description = models.CharField(max_length=255)
    long_description = models.TextField()
    image = models.ImageField(upload_to='company_images')
    category = models.ForeignKey(Category, null=True, blank=False)