from django.db import models


# Create your models here.
class Category(models.Model):
    english_name = models.CharField(max_length=255)
    arabic_name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.english_name


class Company(models.Model):
    english_name = models.CharField(max_length=255, default="", null=True, blank=True)
    arabic_name = models.CharField(max_length=255, default="", null=True, blank=True)
    short_description = models.CharField(max_length=255)
    long_description = models.TextField()
    logo = models.ImageField(upload_to='company_logos', null=True, blank=True)
    image = models.ImageField(upload_to='company_images')
    website = models.CharField(max_length=255, default="", null=True, blank=True)
    category = models.ForeignKey(Category, null=True, blank=False)
    is_active = models.BooleanField(default=True)
    is_promoted = models.BooleanField(default=False)

    def __unicode__(self):
        return self.english_name


class Project(models.Model):
    name = models.CharField(max_length=255, default="", null=True, blank=False)
    address = models.CharField(max_length=255, default="", null=True, blank=False)
    area = models.CharField(max_length=255, default="", null=True, blank=False)
    phone = models.CharField(max_length=255, default="", null=True, blank=False)
    image = models.ImageField(upload_to='company_images')
    company = models.ForeignKey(Company, null=True, blank=False)
    price = models.CharField(max_length=255, default="", null=True, blank=False)
    notes = models.TextField()
    is_approved = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name