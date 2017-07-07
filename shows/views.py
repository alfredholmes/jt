from django.shortcuts import render
from django.http import Http404

import re

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


	return render(request, 'shows/overview.html', {'menu': Category.objects.all().order_by('order'), 'category': category , 'shows': shows, 'text_elements': parseTextElement(category)})

def show(request, category_link, show_link):
	try:
		show = Show.objects.get(link = show_link)
	except:
		raise Http404("Show does not Exist")

	reviews = show.review_set.all()



	return render(request, 'shows/showview.html', {'menu': Category.objects.all().order_by('order'), 'show': show, 'reviews': reviews})

def parseTextElement(category):
		#for text element photo rendering
	#create structure:   [{ 'title' : title, 'data': [{'type': img, 'url': url}, {'type': text, 'content': textcontent}}]
	text_elements = []

	for text in category.textelement_set.all():
		element = {}



		open_pos = [a.start() for a in re.finditer('{\w+}', text.content)]
		close_pos = [a.start() for a in re.finditer('}', text.content)]

		tags = re.findall('{\w+}', text.content)

		element['title'] = text.title
		element['data'] = []
		if len(open_pos) != len(close_pos):
			break
		



		for i in range(0, len(open_pos)):
			if i == 0:
				element['data'].append({'type': 'text', 'data': text.content[0:open_pos[i]]})
			else:
				element['data'].append({'type': 'text', 'data': text.content[close_pos[i-1]+1:open_pos[i]]})

			element['data'].append({'type': 'img', 'data': text.imageelement_set.all().get(tag=tags[i][1:-1]).image.url})

		if len(close_pos) != 0:
			element['data'].append({'type': 'text', 'data': text.content[close_pos[-1]+1:-1]})
		else:
			element['data'].append({'type': 'text', 'data': text.content})

		
		text_elements.append(element)

	return text_elements