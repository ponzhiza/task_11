from typing import Any, Dict, Mapping, Optional, Type, Union
from django import forms
from django.core.exceptions import ValidationError
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from .models import OnlineShop


class AdvertisementForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        self.fields['title'].widget.attrs['class'] = 'form-control form-control-lg'
        self.fields['description'].widget.attrs['class'] = 'form-control form-control-lg'
        self.fields['price'].widget.attrs['class'] = 'form-control form-control-lg'
        self.fields['auction'].widget.attrs['class'] = 'form-control form-control-lg'
        self.fields['image'].widget.attrs['class'] = 'form-control form-control-lg'

    class Meta:
        model = OnlineShop
        fields = ('title', 'description', 'price', 'auction', 'image')

        def clean_title(self):
            super(ValidationError, self).form_valid(self)
