from django.contrib import admin
from .models import ImageElement, Category, Show, Review, TextElement, Post, PostCategory
# Register your models here.

admin.site.register(Category)
admin.site.register(Review)


class ImageElementInline(admin.StackedInline):
	model = ImageElement
	extra = 1


	fields = ( 'image_tag', 'image', 'title', 'description', 'order')
	readonly_fields = ('image_tag',)

class ImageElementTextInline(admin.StackedInline):
	model = ImageElement
	extra = 1
	fields = ('image_tag', 'image', 'title', 'tag')
	readonly_fields = ('image_tag',)


class ReviewElementInline(admin.StackedInline):
	model = Review
	extra = 1

class ShowAdmin(admin.ModelAdmin):
	inlines = [ImageElementInline, ReviewElementInline]

class TextAdmin(admin.ModelAdmin):
	inlines = [ImageElementTextInline]


class PostAdmin(admin.ModelAdmin):
	inlines = [ImageElementTextInline]
	fields = ( 'title', 'category', 'content', 'show')

class CategoryAdmin(admin.ModelAdmin):
	fields = ( 'title', )




admin.site.register(Show, ShowAdmin)
admin.site.register(TextElement, TextAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(PostCategory, CategoryAdmin)
