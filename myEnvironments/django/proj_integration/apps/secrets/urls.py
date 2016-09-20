from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'addSecret$', views.addSecret, name="addSecret"),
    url(r'addLike/(?P<secretID>\d+)$', views.addLike, name="addLike")
]
