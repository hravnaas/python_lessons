from django.shortcuts import render
from ..login_reg.models import User
from .models import Author, Book, Review

def index(request):
    context = {
        'recentReviews' : Review.objects.getRecent(3),
        'reviewedBooks' : Book.objects.withReview()
    }
    return render(request, 'belt_reviewer/index.html', context)

def newBook(request):
    Book.objects.addNew(request.POST)
    return redirect('/')
