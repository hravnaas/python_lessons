from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    #url(r'process_money$', views.processMoney, name="processMoney"),
    url(r'process_money/(?P<building>[a-zA-Z]+)$', views.processMoney, name="processMoney"),
]
