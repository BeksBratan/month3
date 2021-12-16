from django.shortcuts import render
from django.http import Http404, HttpResponse
from bookstore import models, forms



def get_book(request):
    book = models.Book.objects.all()
    return render(request, 'book_list.html', {'book': book})


def book_detail(request, id):
    try:
        book = models.Book.objects.get(id=id)
        try:
            comment = models.Comment.objects.filter(book_id=id).order_by('created_date')
        except models.Comment.DoesNotExist:
            return HttpResponse('No comments')

    except models.Book.DoesNotExist:
        raise Http404('book does not exist, baby')
    return render(request, 'book_detail.html', {'book': book, 'book_comment': comment})


def add_book(request):
    method = request.method
    if method == 'POST':
        form = forms.BookForm(request.POST, request.FILES)
        print(form.data)
        post = models.Book.objects.create(title=form.data['title'],
                                   author=form.data['author'],
                                   description=form.data['description'],
                                   image=form.data['image'])
        post.save()
        return HttpResponse('Book created Successfully')
    else:
        form = forms.BookForm()
    return render(request, 'add_book.html', {'form': form})



def add_comment2(request):
    method = request.method
    if method == 'POST':
        form = forms.CommentForm(request.POST, request.FILES)
        print(form.data)
        if form.is_valid():
            form.save()
            return HttpResponse('Comment created Successfully')
    else:
        form = forms.CommentForm()
    return render(request, 'add_comment2.html', {'form': form})

