from django.shortcuts import render, redirect, reverse
from ..login_reg.models import User
from .models import Author, Book, Review

def index(request):
    if "userID" not in request.session:
        return redirect(reverse('useradmin:index'))
    #return render(request, 'login_reg/index.html')
    context = {
        'recentReviews' : Review.objects.getRecent(3),
        'reviewedBooks' : Book.objects.withReview()
    }
    return render(request, 'belt_reviewer/index.html', context)

def newBook(request):
    Book.objects.addNew(request.POST)
    return redirect('/')
