from __future__ import unicode_literals
from django.db import models
from ..login_reg.models import User


############### Author ###############

class AuthorMgr(models.Manager):
    def addNew(self, data):
        # TODO: Check if author exists before adding.
        return Author.objects.create(
                name = data['author']
            )

    def getAll(self):
        return Author.objects.all()

class Author(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = AuthorMgr()

############### Book ###############

class BookMgr(models.Manager):
    def addNew(self, data):

        # First deal with the author.
        author = None
        if len(data['author']) > 0:
            # We are given a new author name. Add it first.
            author = Author.objects.addNew(data)
        else:
            # Get the author for the passed in existing author (ID).
            author = Author.objects.get(id = data['authorID'])

        # Create the book.
        user = User.objects.get(id = data['userID'])
        book = Book.objects.create(
                title = data['title'],
                author = author,
                user = user
            )

        # Create the review if one was submitted.
        if len(data['review']) > 0:
            review = Review.objects.addNew(data, book.id)

        return book

    # Get all books that have at least one review.
    def withReview(self):
        return Book.objects.all().exclude(book_reviews = None)

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author)
    user = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = BookMgr()


############### Review ###############

class ReviewMgr(models.Manager):
    def addNew(self, data, bookID):
        return Review.objects.create(
                review = data['review'],
                rating = data['rating'],
                book = Book.objects.get(id = bookID),
                user = User.objects.get(id = data['userID'])
            )

    def removeReview(self, data):
        Review.objects.get(id = data['id']).delete()
        return

    # Only get the <numReviews> most recent reviews.
    def getRecent(self, numReviews):
        return Review.objects.all().order_by('-created_at')[:numReviews]

class Review(models.Model):
    review = models.TextField(max_length=1000)
    rating = models.PositiveSmallIntegerField()
    book = models.ForeignKey(Book, related_name = 'book_reviews')
    user = models.ForeignKey(User, related_name = 'user_reviews')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = ReviewMgr()
