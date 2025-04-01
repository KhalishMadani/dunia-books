from django.db import models

# Create your models here.
class Library(models.Model):
    book_name = models.CharField(max_length=100)
    book = models.FileField(upload_to="pdfs/", max_length=100)
    image = models.ImageField(upload_to="img/", blank=True, height_field=None, width_field=None, max_length=None, null=True)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.book_name