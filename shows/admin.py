from django.contrib import admin
from .models import ImageElement, Category, Show, Review, TextElement
# Register your models here.

admin.site.register(Category)
admin.site.register(Review)
admin.site.register(TextElement)

class ImageElementInline(admin.StackedInline):
	model = ImageElement
	extra = 1


	fields = ( 'image_tag', 'image', 'title', 'description')
	readonly_fields = ('image_tag',)

class ReviewElementInline(admin.StackedInline):
	model = Review
	extra = 1

class ShowAdmin(admin.ModelAdmin):
	inlines = [ImageElementInline, ReviewElementInline]



admin.site.register(Show, ShowAdmin)
