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

class Author(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = AuthorMgr()

############### Book ###############

class BookMgr(models.Manager):
    def addNew(self, data):
        return Book.objects.create(
                title = data['title'],
                author = Author.objects.get(id = data['authorID']),
                user = User.objects.get(id = data['userID'])
            )

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
    def addNew(self, data):
        return Review.objects.create(
                review = data['review'],
                rating = data['rating'],
                book = Book.objects.get(id = data['bookID']),
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
