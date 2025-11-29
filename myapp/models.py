from django.db import models
from django.db import models

class PDFFile(models.Model):
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to='pdfs/')
    image = models.ImageField(upload_to='newsniasosi/')
    def __str__(self):
        return self.name