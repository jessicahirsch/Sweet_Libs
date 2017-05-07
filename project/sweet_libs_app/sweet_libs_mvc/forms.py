from django import forms
from .models import Question
from .models import Choice


class PollForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = ('name', )