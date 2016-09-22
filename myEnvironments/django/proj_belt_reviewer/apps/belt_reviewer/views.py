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

# Prompts user to enter information for a new book and optional review.
def addBook(request):
    return render(request, 'belt_reviewer/addBook.html', { 'authors' : Author.objects.getAll() })

# Stores a new book and optionally a review.
def createBook(request):
    print "DEBUG: Entering createBook"
    if request.method == 'POST':
        Book.objects.addNew(request.POST)
    return redirect(reverse('books:index'))
