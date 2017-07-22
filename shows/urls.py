from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^home/$', views.index),
	url(r'^blog/$', views.blog_overview, name='blog'),
	url(r'^blog/(?P<category_link>[-\w+]+)$', views.blog_category, name='blog_category'),
	url(r'^blog/post/(?P<post_link>[-\w+]+)', views.blog_detail, name='blog_detail'),
	url(r'^(?P<category_link>[-\w+]+)/$', views.overview, name='overview'),
	url(r'^(?P<category_link>[-\w+]+)/(?P<show_link>[\w+]+)$', views.show, name='show'),

]
