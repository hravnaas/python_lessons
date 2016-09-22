from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'add/$', views.addBook, name="addBook"),
    url(r'create/$', views.createBook, name="createBook")
]
