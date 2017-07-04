from django.shortcuts import render
from django.http import Http404

from .models import ImageElement, Category, Show
# Create your views here.


def index(request):
	featured = Show.objects.filter(homepage=True).order_by('start_date')
	context = {'menu': Category.objects.all(), 'featured' : featured}
	return render(request, 'shows/index.html', context)

def overview(request, category_link):
	try:
		category = Category.objects.get(link=category_link)
		shows = category.show_set.all()
	except Show.DoesNotExist:
		raise Http404("Category does not exist")
	return render(request, 'shows/overview.html', {'menu': Category.objects.all(), 'category': category, 'shows': shows})

def show(request, category, show_id):
	return