from django.db import models

# Create your models here.

class Category(models.Model):
	title = models.CharField(max_length=200)
	link = models.CharField(max_length=200)

	def __str__(self):
		return self.title

class Show(models.Model):
	category = models.ForeignKey(Category, on_delete = models.PROTECT, null=True)
	title = models.CharField(max_length=200)
	start_date = models.DateField()
	end_date = models.DateField()
	director = models.CharField(max_length=200)
	company = models.CharField(max_length=200)
	description = models.TextField()


	def __str__(self):
		return self.title




class ImageElement(models.Model):
	show = models.ForeignKey(Show, on_delete = models.CASCADE, null=True)
	title = models.CharField(max_length=200)
	description = models.TextField()
	image = models.ImageField(upload_to='show_images/')

	def __str__(self):
		return self.title
