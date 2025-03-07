from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    BooksList,
    BookCreate,
    BookDetail,
    BookUpdate,
    BookDelete,
)

urlpatterns = [
    path('', BooksList.as_view(), name='list'),
    path('book-create/', BookCreate.as_view(), name='book-create'),
    path('book-detail/<int:pk>', BookDetail.as_view(), name='book-detail'),
    path('book-update/<int:pk>', BookUpdate.as_view(), name='book-update'),
    path('book-delete/<int:pk>', BookDelete.as_view(), name='book-delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)