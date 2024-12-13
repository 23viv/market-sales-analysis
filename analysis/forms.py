from django import forms
from .models import ExcelFile, FileUpload

class ExcelFileForm(forms.ModelForm):
    class Meta:
        model = ExcelFile
        fields = ['file']  # Include only the file field
        widgets = {
            'file': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'file': 'Upload Excel File',
        }

class FileUploadForm(forms.ModelForm):
    class Meta:
        model = FileUpload
        fields = ['file']  # Include only the file field
        widgets = {
            'file': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'file': 'Upload File',
        }
