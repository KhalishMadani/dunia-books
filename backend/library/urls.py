from django.urls import path
from .views import LibraryView, LibraryList, LibraryFileResponse

urlpatterns = [
    path(
        '',
        LibraryView.as_view()
    ),
    
    path(
        'library-list/',
        LibraryList.as_view(),
        name='library_list'
    )
]
