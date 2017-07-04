from django.shortcuts import render

from .models import ImageElement
# Create your views here.


def index(request):
	ies = ImageElement.objects.all()
	context = {'images' : ies}
	return render(request, 'shows/index.html', context)