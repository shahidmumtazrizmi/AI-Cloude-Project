from django import forms
from .models import StorageBucket, StorageFile

class StorageBucketForm(forms.ModelForm):
    class Meta:
        model = StorageBucket
        fields = ['name', 'description', 'is_public']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full px-3 py-2 border border-gray-300 rounded-md', 'placeholder': 'Bucket Name'}),
            'description': forms.Textarea(attrs={'class': 'w-full px-3 py-2 border border-gray-300 rounded-md', 'rows': 2, 'placeholder': 'Description (optional)'}),
            'is_public': forms.CheckboxInput(attrs={'class': 'ml-2'}),
        }

class FileUploadForm(forms.ModelForm):
    class Meta:
        model = StorageFile
        fields = ['name', 'file', 'mime_type']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full px-3 py-2 border border-gray-300 rounded-md', 'placeholder': 'File Name'}),
            'file': forms.ClearableFileInput(attrs={'class': 'w-full px-3 py-2 border border-gray-300 rounded-md'}),
            'mime_type': forms.TextInput(attrs={'class': 'w-full px-3 py-2 border border-gray-300 rounded-md', 'placeholder': 'MIME Type'}),
        } 