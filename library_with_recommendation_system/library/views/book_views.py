from rest_framework import generics, permissions

from library.models import Book
from library.serializers.book_serializers import BookSerializer

class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

def get_queryset(self):
    queryset = Book.objects.all()
    query = self.request.query_params.get('search')
    if query:
        queryset = queryset.filter(title__icontains=query) | queryset.filter(author__name__icontains=query)
    return queryset
