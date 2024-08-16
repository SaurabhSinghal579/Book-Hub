from django.contrib import admin

from .models import Book, Recommendation,Like,Comment
admin.site.register(Book)
admin.site.register(Recommendation)
admin.site.register(Like)
admin.site.register(Comment)
