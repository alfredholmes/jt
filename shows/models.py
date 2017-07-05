from django.db import models

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



class ImageElement(models.Model):
	show = models.ForeignKey(Show, on_delete = models.CASCADE, null=True)
	title = models.CharField(max_length=200, null=True)
	description = models.TextField(null=True)
	image = models.ImageField(upload_to='show_images/')
	order = models.IntegerField()
	


	def image_tag(self):
		return u'<image src="%s" height="200"/>' % self.image.url

	image_tag.short_description = 'Image'
	image_tag.allow_tags = True

	def __str__(self):
		return self.show.title + " - " + self.title


class TextElement(models.Model):
	category = models.ForeignKey(Category, on_delete=models.PROTECT)
	title = models.CharField(max_length=200)
	content = models.TextField()

	def __str__(self):
		return self.category.title + " - " + self.title
