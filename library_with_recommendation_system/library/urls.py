from django.urls import path

from library.views.author_views import AuthorDetail, AuthorList
from library.views.book_views import BookDetail, BookList

urlpatterns = [
    # Book routes
    path('', BookList.as_view(), name='book-list'),
    path('<int:id>/', BookDetail.as_view(), name='book-detail'),

    # Author routes
    path('authors/', AuthorList.as_view(), name='author-list'),
    path('authors/<int:id>/', AuthorDetail.as_view(), name='author-detail'),

  
]