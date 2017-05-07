from django import forms

from .models import Choice

class ChoiceForm(forms.ModelForm):
    class Meta:
        db_table = u'Choice Table'
        CHOICES = (('Option 1', 'Option 1'),('Option 2', 'Option 2'),)
        field = forms.ChoiceField(choices=CHOICES)
