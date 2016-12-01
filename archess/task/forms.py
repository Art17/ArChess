from django import forms
from .models import Task


class TaskCreationForm(forms.ModelForm):
    question = forms.CharField(
        widget=forms.Textarea()
    )
    class Meta:
        model = Task
        fields = ['title', 'start_pos', 'question', 'difficulty']


class TaskSearchForm(forms.Form):
    author = forms.CharField(max_length=20)