from django.db import models

# Create your models here.
class Library(models.Model):
    book_name = models.CharField(max_length=50)
    book = models.FileField(upload_to="pdfs/", max_length=100)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)