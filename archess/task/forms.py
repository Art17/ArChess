from django import forms
from .models import Task


class TaskCreationForm(forms.ModelForm):
    start_pos = forms.CharField(
        widget=forms.TextInput(attrs={'readonly': 'readonly'})
    )
    question = forms.CharField(
        widget=forms.Textarea()
    )
    class Meta:
        model = Task
        fields = ['title', 'start_pos', 'question', 'difficulty']
        readonly_fields = ['start_pos']


class TaskSearchForm(forms.Form):
    author = forms.CharField(max_length=20)