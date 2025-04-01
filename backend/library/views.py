from rest_framework.views import APIView
from rest_framework.response import Response

from django.http import FileResponse
from django.views import View
from django.views.generic.list import ListView
from django.shortcuts import get_object_or_404

from django.utils.decorators import method_decorator
from django.views.decorators.clickjacking import xframe_options_sameorigin, xframe_options_exempt

from .models import Library
from .serializer import LibrarySerializer

# Create your views here.
class LibraryView(APIView):
    # @xframe_options_sameorigin
    def get(self, request):
        query = Library.objects.all()
        serializer = LibrarySerializer(query, many=True)
        return Response( {'data': serializer.data} )


class LibraryList(ListView):
    template_name = 'show_pdf.html'
    model = Library
    context_object_name = 'library'

class LibraryFileResponse(View):
    template = "show_pdf.html"

    def get(self, request, pk):
        query = get_object_or_404(Library, pk=pk)
        return FileResponse(
            query.book.open('rb'),
            content_type="application/pdf",
            as_attachment=True
        )