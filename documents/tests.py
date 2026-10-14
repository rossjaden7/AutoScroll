from io import BytesIO

from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.urls import reverse

from .models import Document


class DocumentUploadTests(TestCase):

    def test_upload_pdf_creates_document_and_returns_document_page(self):
        pdf = SimpleUploadedFile(
            "test.pdf",
            b"%PDF-1.4 test pdf content",
            content_type="application/pdf",
        )

        response = self.client.post(
            reverse("upload"),
            {"file": pdf},
        )

        document = Document.objects.get(filename="test.pdf")

        self.assertRedirects(
            response,
            reverse("document", args=[document.id]),
        )

        self.assertTrue(document.file.name)

        response = self.client.get(
            reverse("document", args=[document.id])
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "test.pdf")