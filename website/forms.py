from django import forms
from django.forms import ModelForm
from .models import Softmatterdata
import datetime

class dataForm(ModelForm):
    class Meta:
        model = Softmatterdata
        fields = ('composition', 'method', 'doi', 'summary', 'sample_image', 'meta_data')
        labels = {
            'composition': 'Material Composition',
            'method':'Acquisition Method',
            'doi':'DOI',
            'summary':'Summary',
            'sample_image':'Sample Image',
            'meta_data':'Meta Data',
        }

        widgets = {
            'composition': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Material Composition'}),
            'method': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Acquisition Method'}),
            'doi': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'DOI'}),
            'summary':forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Summary'}),
            'sample_image':'',
            'meta_data':'',
        }

class addForm(ModelForm):
    class Meta:
        model = Softmatterdata
        fields = ('composition', 'method', 'name', 'acquired', 'doi', 'summary', 'sample_image', 'meta_data')
        labels = {
            'composition': 'Material Composition',
            'method':'Acquisition Method',
            'name':'Name',
            'acquired':'Aquisition Date',
            'doi':'DOI',
            'summary':'Summary',
            'sample_image':'Sample Image',
            'meta_data':'Meta Data',
        }

        widgets = {
            'composition': forms.TextInput(attrs={'class':'form-control'}),
            'method':forms.TextInput(attrs={'class':'form-control'}),
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'acquired': forms.DateInput(attrs={'class':'form-control', 'type':'date'}),
            'doi': forms.TextInput(attrs={'class':'form-control'}),
            'summary': forms.TextInput(attrs={'class':'form-control'}),
            'sample_image':'',
            'meta_data':'',
        }

