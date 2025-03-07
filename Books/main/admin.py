from django.contrib import admin
from .models import Book

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'genre', 'publisher', 'price', 'quantity')
    search_fields = ('title', 'author', 'genre', 'publisher')
    list_filter = ('title', 'author', 'genre', 'publisher')
    ordering = ('id',)

admin.site.register(Book, BookAdmin)