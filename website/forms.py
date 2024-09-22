from django import forms
from django.forms import ModelForm
from .models import Softmatterdata
from django.core.exceptions import ValidationError
import datetime

composition_choices = [

    ("actin", "actin"),
    ("microtubules", "microtubules"),
    ("crosslinkers", "crosslinkers"),
    ("DNA", "DNA"),
    ("kinesin", "kinesin"),
    ("myosin", "myosin"),
    ("hydrogel", "hydrogel"),
    ("colloids", "colloids"),
    ("ASE1", "ASE1"),
    ("cells", "cells"),
    ("phalloidin", "phalloidin"),
    ("taxol", "taxol"),
    ("GMPCPP", "GMPCPP"),
    ("other", "other"),
]

acquisition_choices = [
    ("epifluorescence", "epifluorescence"),
    ("confocal", "confocal"),
    ("optical tweezers", "optical tweezers"),
    ("rheometer", "rheometer"),
    ("light sheet", "light sheet"),
    ("bright field", "bright field"),
    ("TIRF", "TIRF"),
    ("DLS", "DLS"),
    ("other", "other"),
]

def file_size(value): # add this to some file where you can import it from
    limit = 2 * 1024 * 1024
    if value.size > limit:
        raise ValidationError('File too large. Size should not exceed 2 MiB.')
    
class dataForm(ModelForm):
    composition =  forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                          choices=composition_choices, label='Material Composition')
    method = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                          choices=acquisition_choices, label='Acquisition Method')
    class Meta:
        model = Softmatterdata
        fields = ('composition', 'method', 'doi', 'summary', 'sample_image', 'meta_data', 'additional_resources1', 'additional_resources2', 'additional_resources3', 'barcode', 'barcode_display')
        labels = {
            'composition': 'Material Composition',
            'method':'Acquisition Method',
            'doi':'DOI',
            'summary':'Experimental Protocol Details',
            'sample_image':'Sample Image',
            'meta_data':'Metadata',
            'additional_resources1':'Additional Files',
            'additional_resources2':'',
            'additional_resources3':'',
            'barcode':'Barcode File',
            'barcode_display':'Barcode Display'
        }

        widgets = {
            'doi': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'DOI'}),
            'summary':forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Summary'}),
            'header':'',
            'sample_image':'',
            'meta_data':'',
            'additional_resources1':forms.ClearableFileInput(attrs={'class': 'form-control-file', 'required': False, 'validators': [file_size]}),
            'additional_resources2':forms.ClearableFileInput(attrs={'class': 'form-control-file', 'required': False, 'validators': [file_size]}),
            'additional_resources3':forms.ClearableFileInput(attrs={'class': 'form-control-file', 'required': False, 'validators': [file_size]}),
            'barcode':'',
            'barcode_display':''
        }

class addForm(ModelForm):
    composition =  forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                          choices=composition_choices, label='Material Composition')
    method = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                          choices=acquisition_choices, label='Acquisition Method')
    class Meta:
        model = Softmatterdata
        fields = ('composition', 'method', 'acquired', 'doi', 'summary', 'sample_image', 'meta_data', 'additional_resources1', 'additional_resources2', 'additional_resources3', 'barcode', 'barcode_display')
        labels = {
            'composition': 'Material Composition',
            'method':'Acquisition Method',
            'acquired':'Acquisition Date',
            'doi':'DOI',
            'summary':'Experimental Protocol Details',
            'sample_image':'Sample Image',
            'meta_data':'Metadata',
            'additional_resources1':'Additional Files',
            'additional_resources2':'',
            'additional_resources3':'',
            'barcode':'Barcode File',
            'barcode_display':'Barcode Display'
        }

        widgets = {
            'acquired': forms.DateInput(attrs={'class':'form-control', 'type':'date'}),
            'doi': forms.TextInput(attrs={'class':'form-control'}),
            'summary': forms.TextInput(attrs={'class':'form-control'}),
            'sample_image':'',
            'meta_data':'',
            'additional_resources1':forms.ClearableFileInput(attrs={'class': 'form-control-file', 'required': False, 'validators': [file_size]}),
            'additional_resources2':forms.ClearableFileInput(attrs={'class': 'form-control-file', 'required': False, 'validators': [file_size]}),
            'additional_resources3':forms.ClearableFileInput(attrs={'class': 'form-control-file', 'required': False, 'validators': [file_size]}),
            'barcode':'',
            'barcode_display':''
        }


    def clean_acquired(self):
        acquired_date = self.cleaned_data.get('acquired')
        if acquired_date and acquired_date > datetime.date.today():
            raise ValidationError('Acquisition date cannot be in the future.')
        return acquired_date


