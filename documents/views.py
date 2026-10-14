from django.shortcuts import get_object_or_404, redirect, render

from .models import Document


def upload_document(request):
    if request.method == "POST":
        uploaded_file = request.FILES["file"]

        document = Document.objects.create(
            filename=uploaded_file.name,
            file=uploaded_file,
        )

        return redirect("document", document_id=document.id)

    return render(request, "documents/upload.html")


def document_view(request, document_id):
    document = get_object_or_404(Document, id=document_id)
    return render(
        request,
        "documents/document.html",
        {"document": document},
    )