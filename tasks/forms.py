
from django import forms

class BulkTaskAddForm(forms.Form):
    tasks = forms.CharField(widget=forms.Textarea(attrs={'class': 'formclass'}))