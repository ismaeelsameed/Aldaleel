from django.contrib import admin

# Register your models here.
from aldaleel.models import Company, Category

admin.site.register(Company)
admin.site.register(Category)