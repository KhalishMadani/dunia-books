from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Library
from .serializer import LibrarySerializer

# Create your views here.
class LibraryView(APIView):
    def get(self, request):
        query = Library.objects.all()
        serializer = LibrarySerializer(query, many=True)
        return Response( {'data': serializer.data} )