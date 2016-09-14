from django.conf.urls import url
from . import views

# def index(request):
# 	print("I'm running")

urlpatterns = [
    url(r'^$', views.index, name="index")
]