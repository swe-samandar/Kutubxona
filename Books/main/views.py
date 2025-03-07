from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.db.models import Q
from .forms import BookForm
from .models import Book

class BookCreate(View):
    def get(self, request):
        form = BookForm()
        return render(request, 'book_create.html', {'form': form})
    

    def post(self, request):
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list')
        return render(request, 'book_create.html', {'form': form})

class BooksList(View):
    def get(self, request):
        query = request.GET.get('q')
        books = Book.objects.filter(Q(title__icontains=query) | Q(author__icontains=query) | Q(genre__icontains=query)) if query else Book.objects.all()
        return render(request, 'list.html', {'books': books})
    

class BookDetail(View):
    def get(self, request, pk):
        book = get_object_or_404(Book, id=pk)
        return render(request, 'book_detail.html', {'book': book})


class BookUpdate(View):
    def get(self, request, pk):
        book = get_object_or_404(Book, id=pk)
        form = BookForm(instance=book)
        return render(request, 'book_update.html', {'form': form})

    def post(self, request, pk):
        book = get_object_or_404(Book, id=pk)
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book-detail', pk=pk)
        return render(request, 'book_update.html', {'form': form})



class BookDelete(View):
    def get(self, request, pk):
        book = get_object_or_404(Book, id=pk)
        return render(request, 'book_delete.html', {'book': book})

    def post(self, request, pk):
        book = get_object_or_404(Book, id=pk)
        if request.method == 'POST':
            book.delete()
            return redirect('list')
        return render(request, 'book_delete.html', {'book': book})
