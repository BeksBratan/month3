

from django.urls import path
from bookstore import views

urlpatterns = [
    path('', views.get_book, name='book_view'),
    path('<int:id>/', views.book_detail, name='book_detail_view'),


]