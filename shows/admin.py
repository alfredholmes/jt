from django.contrib import admin
from .models import ImageElement, Category, Show, Review
# Register your models here.

admin.site.register(ImageElement)
admin.site.register(Category)
admin.site.register(Show)
admin.site.register(Review)