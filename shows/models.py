from django.db import models

# Create your models here.

class Category(models.Model):
	title = models.CharField(max_length=200)
	link = models.CharField(max_length=200)
	order = models.IntegerField()

	def __str__(self):
		return self.title

	class Meta:
		verbose_name_plural = "categories"

class Show(models.Model):
	category = models.ForeignKey(Category, on_delete = models.PROTECT, null=True)
	title = models.CharField(max_length=200)
	link = models.CharField(max_length=200)
	start_date = models.DateField()
	end_date = models.DateField()
	director = models.CharField(max_length=200)
	company = models.CharField(max_length=200)
	description = models.TextField()
	homepage = models.BooleanField()
	company_page = models.CharField(max_length=300)

	
	poster = models.ImageField(upload_to='show_posters/')


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
	title = models.CharField(max_length=200)
	description = models.TextField()
	image = models.ImageField(upload_to='show_images/')

	def __str__(self):
		return self.title


