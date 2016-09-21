from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"), # Could you class based views here to avoid having multiple routes.
    url(r'^(?P<id>\d+)$', views.show, name="show"),
    url(r'^new$', views.new, name="new"),
    url(r'^(?P<id>\d+)/edit$', views.edit, name="edit"),
    url(r'^create$', views.create, name="create"), # TODO FIX
    url(r'^update/(?P<id>\d+)$', views.update, name="update"),
    url(r'^destroy/(?P<id>\d+)$', views.destroy, name="destroy")
]
