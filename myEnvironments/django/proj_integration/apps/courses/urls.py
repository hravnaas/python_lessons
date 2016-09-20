from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'destroy/(?P<courseID>\d+)$', views.removeCourse, name = 'removeCourse'),
    url(r'destroy/(?P<courseID>\d+)/confirm$', views.CourseRemoveConfirmation, name = 'CourseRemoveConfirmation'),
    url(r'add$', views.addCourse, name = 'addCourse'),
    url(r'users_courses$', views.addUserToCourse, name = 'addUserToCourse'),
    url(r'link_user_course$', views.linkUserToCourse, name = 'linkUserToCourse')
]
