from rest_framework import serializers

from library.serializers.author_serializers import AuthorSerializer
from library.models import Book, FavoriteBook


class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()

    class Meta:
        model = Book
        fields = ["id", "title", "description", "author"]


class FavoriteBookSerializer(serializers.ModelSerializer):
    book = BookSerializer()

    class Meta:
        model = FavoriteBook
        fields = ["book", "added_at"]
