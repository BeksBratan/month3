

from django.urls import path
from bookstore import views

urlpatterns = [
    path('', views.get_book, name='book_view'),
    path('<int:id>/', views.book_detail, name='book_detail_view'),
    path('add-book/', views.add_book, name='add_book_view'),
    path('add-comment-book/', views.add_comment2, name='add_comment_book_view'),


]
