from rest_framework import serializers
from .models import Library

class LibrarySerializer(serializers.ModelSerializer):
    book = serializers.SerializerMethodField()

    def get_book(self, obj):
        return obj.book.url if obj.book else None
    
    class Meta:
        model = Library
        fields = [
            'book_name',
            'book',
            'created_at'
        ]