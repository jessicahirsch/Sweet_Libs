from django import forms

from .models import Choice

class ChoiceForm(forms.ModelForm):
    class Meta:
        db_table = u'Choice Table'
        CHOICES = (('Choice', 'Choice'),)
        field = forms.ChoiceField(choices=CHOICES)
