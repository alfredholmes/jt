from django.shortcuts import render
from django.http import Http404

from .models import ImageElement, Category, Show
# Create your views here.


def index(request):
	try:
		featured = Show.objects.filter(homepage=True).order_by('-start_date')
		context = {'menu': Category.objects.all().order_by('order'), 'featured' : featured}
	except Show.DoesNotExist:
		raise Http404("Error, missing shows")
	except Category.DoesNotExist:
		raise Http404("Error, missing Category")
	return render(request, 'shows/index.html', context)

def overview(request, category_link):
	try:
		category = Category.objects.get(link=category_link)
		shows = category.show_set.all()
	except Category.DoesNotExist:
		raise Http404("Category does not exist")
	except Show.DoesNotExist:
		raise Http404("Show does not exist")

	return render(request, 'shows/overview.html', {'menu': Category.objects.all().order_by('order'), 'category': category , 'shows': shows})

def show(request, category_link, show_link):
	try:
		show = Show.objects.get(link = show_link)
	except:
		raise Http404("Show does not Exist")

	reviews = show.review_set.all()

	return render(request, 'shows/showview.html', {'menu': Category.objects.all().order_by('order'), 'show': show, 'reviews': reviews})