from django.shortcuts import render
from django.http import Http404
from bookstore import models

def get_book(request):
    book = models.Book.objects.all()
    return render(request, 'book_list.html', {'book': book})

def book_detail(request, id):
    try:
        book = models.Book.objects.get(id=id)
    except models.Book.DoesNotExist:
        raise Http404('Book does not exist!')
    return render(request, 'book_detail.html', {'book': book})



