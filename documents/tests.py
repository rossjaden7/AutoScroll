from django.test import TestCase
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from documents.models import Document


class DocumentUploadTests(TestCase):

    def test_document_page_shows_uploaded_pdf(self):
        document = Document.objects.create(
            file=SimpleUploadedFile(
                "test.pdf",
                b"PDF content",
                content_type="application/pdf",
            ),
        )

        response = self.client.get(
            reverse("document", args=[document.id])
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "<iframe", html=False)

    def test_document_page_returns_404_for_missing_document(self):
        response = self.client.get(
            reverse("document", args=[99999])
        )

        self.assertEqual(response.status_code, 404)

    def test_document_page_displays_requested_document(self):
        first = Document.objects.create(
            file=SimpleUploadedFile(
                "first.pdf",
                b"First PDF",
                content_type="application/pdf",
            ),
        )

        second = Document.objects.create(
            file=SimpleUploadedFile(
                "second.pdf",
                b"Second PDF",
                content_type="application/pdf",
            ),
        )

        response = self.client.get(
            reverse("document", args=[second.id])
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, second.file.name)
        self.assertNotContains(response, first.file.name)