from django import forms
from django.core.validators import ValidationError


class ContactUsForm(forms.Form):
    body = forms.CharField(max_length=500, label='write your messeage')


    def clean(self):
        body = self.cleaned_data.get('body')
        if '/' in body:
            raise ValidationError('only numbers and a-z can be used', code=150_1)
