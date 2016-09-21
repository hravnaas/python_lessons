from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^(?P<id>\d+)$', views.show, name="show"),
    url(r'^new$', views.new, name="new"),
    url(r'^(?P<id>\d+)/edit$', views.edit, name="edit"),
    url(r'^create$', views.create, name="create"), # TODO FIX
    url(r'^(?P<id>\d+)/update$', views.update, name="update"),
    url(r'^(?P<id>\d+)/destroy$', views.destroy, name="destroy")
]
