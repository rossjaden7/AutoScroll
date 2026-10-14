from django.urls import path

from . import views

urlpatterns = [
    path("", views.upload_document, name="upload"),
    path(
        "document/<int:document_id>/",
        views.document_view,
        name="document",
    ),
]