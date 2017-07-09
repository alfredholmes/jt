from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^home/$', views.index),
	url(r'^(?P<category_link>[\w+]+)/$', views.overview, name='overview'),
	url(r'^(?P<category_link>[\w+]+)/(?P<show_link>[\w+]+)$', views.show, name='show'),

]