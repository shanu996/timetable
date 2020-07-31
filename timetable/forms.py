from django import forms
from .models import Tables
class HomeForm(forms.ModelForm):
    table = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a post...'
        }
    ))

    class Meta:
        model = Tables
        fields = ('table',)