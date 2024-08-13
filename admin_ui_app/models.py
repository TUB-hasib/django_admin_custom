from django.db import models

# Create your models here.

class Excel_files_model(models.Model):
    file_name = models.CharField(max_length=20)
    file = models.FileField(upload_to=None)
    
    def __str__(self):
        return self.file_name
