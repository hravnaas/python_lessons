from __future__ import unicode_literals
from django.db import models
from ..login_reg.models import User
#from .models import Course, Description, Comment


class Course(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ManyToManyField(User, related_name = 'courses')


class Description(models.Model):
    description = models.CharField(max_length=200)
    course = models.ForeignKey(Course, related_name = 'myDescription')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# NOTE: Comment is currently not being used.
class Comment(models.Model):
    comment = models.CharField(max_length=200)
    course = models.ForeignKey(Course)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
