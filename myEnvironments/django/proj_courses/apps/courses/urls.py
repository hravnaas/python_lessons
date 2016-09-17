from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^courses/destroy/(?P<courseID>\d+)$', views.removeCourse, name = 'removeCourse'),
    url(r'^courses/destroy/(?P<courseID>\d+)/confirm$', views.CourseRemoveConfirmation, name = 'CourseRemoveConfirmation'),
    url(r'^courses/add$', views.addCourse, name = 'addCourse')
]
