from django.shortcuts import render, get_object_or_404
from django.http import Http404

import re

from .models import ImageElement, Category, Show, Post, PostCategory
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

	#TODO add recent blog posts

	return render(request, 'shows/overview.html', {'menu': Category.objects.all().order_by('order'), 'category': category , 'shows': shows, 'text_elements': parseTextElement(category)})

def show(request, category_link, show_link):
	try:
		show = Show.objects.get(link = show_link)
	except:
		raise Http404("Show does not Exist")

	reviews = show.review_set.all()

	posts = show.post_set.all()

	return render(request, 'shows/showview.html', {'menu': Category.objects.all().order_by('order'), 'show': show, 'reviews': reviews, 'posts': posts})


def parseMediaText(text, text_element=None, post=None):
	if text_element==None and post==None:
		return
	element = {}

	open_pos = [a.start() for a in re.finditer('{(.*?)}', text)]
	close_pos = [a.start() for a in re.finditer('}', text)]

	tags = re.findall('{(.*?)}', text)

	if text_element != None:
		element['title'] = text_element.title
	elif post != None:
		element['title'] = post.title

	element['data'] = []
	if len(open_pos) != len(close_pos):
		return



	for i in range(0, len(open_pos)):
		if i == 0:
			element['data'].append({'type': 'text', 'data': text[0:open_pos[i]]})
		else:
			element['data'].append({'type': 'text', 'data': text[close_pos[i-1]+1:open_pos[i]]})
		if text_element != None:
			element['data'].append(processTag(tags[i], text=text_element))
		elif post != None:
			element['data'].append(processTag(tags[i], post=post))
	if len(close_pos) != 0:
		element['data'].append({'type': 'text', 'data': text[close_pos[-1]+1:-1]})
	else:
		element['data'].append({'type': 'text', 'data': text})

	return element


def blog_overview(request):
	context = {'menu': Category.objects.all().order_by('order')}

	posts = Post.objects.all().order_by('-date_published')[:3]
	data = []
	for post in posts:
		p = parseMediaText(post=post, text=post.content)
		p['link'] = post.link
		if post.imageelement_set.all().count() > 0:
			p['image'] = post.imageelement_set.all()[0]

		p['text'] = ""
		for element in p['data']:
			try:
				if element['type'] == 'text':
					p['text'] = p['text'] + element['data']
			except:
				pass
		if p is not None:
			data.append(p)

	context['posts'] = data
	context['categories'] = []
	for category in PostCategory.objects.all():
		if category.post_set.all().count() > 0:
			context['categories'].append(category)
	return render(request, 'shows/blog.html', context)

def blog_detail(request, post_link):
	post = get_object_or_404(Post, link=post_link)
	p = parseMediaText(post=post, text=post.content)
	return render(request, 'shows/blogview.html', {'menu': Category.objects.all().order_by('order'), 'post': p})

def blog_category(request, category_link):
	pass

def processTag(tag, text=None, post=None):
	value = {'type': 'NULL', 'data': 0}
	try:
		command = tag.split()[0][0:-1]
		data = tag.split()[1:]
	except:
		pass

	if command == 'image':
		if text != None:
			value['type'] = 'img'
			value['data'] = text.imageelement_set.all().get(tag=data[0]).image.url
		elif post != None:
			value['type'] = 'img'
			value['data'] = post.imageelement_set.all().get(tag=data[0]).image.url
	elif command == 'link' and len(data) > 1:
		value['type'] = 'link'
		s = ''
		for a in data[1:]:
			s = s + ' ' + a
		value['data'] = '<a href="' + data[0] + '" target="_blank">' + s + "</a>"

	return value



def parseTextElement(category):
		#for text element photo rendering
	#create structure:   [{ 'title' : title, 'data': [{'type': img, 'url': url}, {'type': 'text', 'content': textcontent}}]
	text_elements = []

	for text in category.textelement_set.all():


		text_elements.append(parseMediaText(text.content, text_element=text))

	return text_elements
