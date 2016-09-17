from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^addEmail$', views.addEmail, name = 'addEmail'),
    url(r'^showAllEmails/(?P<email>.+)$', views.showAllEmails, name = 'showAllEmails')
]
