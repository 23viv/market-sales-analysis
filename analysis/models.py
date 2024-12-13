from django.db import models

class ExcelFile(models.Model):
    file = models.FileField(upload_to='uploads/')  # File field to upload Excel files
    uploaded_at = models.DateTimeField(auto_now_add=True)  # Timestamp for when the file was uploaded

    def __str__(self):
        return f"File {self.file.name} uploaded at {self.uploaded_at}"


class FileUpload(models.Model):
    file = models.FileField(upload_to='uploads/')  # File field to upload general files
    uploaded_at = models.DateTimeField(auto_now_add=True)  # Timestamp for upload time

    def __str__(self):
        return f"File {self.file.name} uploaded at {self.uploaded_at}"
