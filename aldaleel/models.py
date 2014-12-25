from django.db import models


# Create your models here.
class Category(models.Model):
    english_name = models.CharField(max_length=255)
    arabic_name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.english_name


class Company(models.Model):
    name = models.CharField(max_length=255)
    short_description = models.CharField(max_length=255)
    long_description = models.TextField()
    image = models.ImageField(upload_to='company_images')
    category = models.ForeignKey(Category, null=True, blank=False)
    is_active = models.BooleanField(default=True)
    is_promoted = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name