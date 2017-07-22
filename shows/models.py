from django.db import models
from django.template.defaultfilters import slugify
import datetime

# Create your models here.

class Category(models.Model):
	title = models.CharField(max_length=200)
	link = models.CharField(max_length=200)
	order = models.IntegerField(unique=True)

	def __str__(self):
		return self.title

	class Meta:
		verbose_name_plural = "categories"

class Show(models.Model):
	category = models.ForeignKey(Category, on_delete = models.PROTECT, null=True)
	title = models.CharField(max_length=200)
	link = models.CharField(max_length=200, unique=True)
	start_date = models.DateField()
	end_date = models.DateField()
	director = models.CharField(max_length=200)
	company = models.CharField(max_length=200)
	description = models.TextField()
	homepage = models.BooleanField()
	company_page = models.CharField(max_length=300)
	site_live = models.BooleanField(null=False, default=False)


	poster = models.ImageField(upload_to='show_posters/')

	@property
	def main_image(self):
		try:
			image = self.imageelement_set.all().order_by('order')[0]
		except IndexError:
			return 0
		return image

	@property
	def images(self):
		return self.imageelement_set.all().order_by('order')

	def __str__(self):
		return self.title



class Review(models.Model):
	show = models.ForeignKey(Show, on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	content = models.TextField()
	publisher = models.CharField(max_length=200)
	link = models.CharField(max_length=300)


class PostCategory(models.Model):
	title = models.CharField(max_length=50)
	link = models.CharField(max_length=50)
	def save(self, *args, **kwargs):
		self.link = slugify(self.title)
		super().save(*args, **kwargs)

	def __str__(self):
		return self.title

class Post(models.Model):
	title = models.CharField(max_length=200)
	link = models.CharField(max_length=200)
	category = models.ForeignKey(PostCategory, on_delete=models.PROTECT)
	show = models.ForeignKey(Show, on_delete=models.PROTECT, null=True, blank=True)
	content = models.TextField()
	date_published = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title

	def save(self, *args, **kwargs):
		self.link = slugify(self.title)
		super().save(*args, **kwargs)

class TextElement(models.Model):
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	content = models.TextField()

	def __str__(self):
		return self.category.title + " - " + self.title

def photo_directory_path(instance, filename):
	if instance.show is not None:
		return 'show_images/show_{0}/{1}'.format(instance.show.id, filename)
	if instance.text_element is not None:
		return 'page_images/page_{0}/{1}'.format(instance.text_element.id, filename)
	if instance.post is not None:
		return 'blog_images/post_{0}/{1}'.format(instance.post.id, filename)

class ImageElement(models.Model):
	show = models.ForeignKey(Show, on_delete = models.CASCADE, null=True)
	text_element = models.ForeignKey(TextElement, on_delete=models.CASCADE, null=True)
	post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
	title = models.CharField(max_length=200, blank=True)
	description = models.TextField(null=True, blank=True)
	image = models.ImageField(upload_to=photo_directory_path)
	order = models.IntegerField(default=0)
	tag = models.CharField(max_length=200, null=True)



	def image_tag(self):
		return u'<image src="%s" height="200"/>' % self.image.url

	image_tag.short_description = 'Image'
	image_tag.allow_tags = True

	def __str__(self):
		try:
			return self.show.title + " - " + self.title
		except:
			return ''
