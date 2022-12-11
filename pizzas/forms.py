from django import forms

from .models import *

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']
        labels = {'text':''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}