from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Title', 'class': 'title-field'}),
            'content': forms.Textarea(attrs={'placeholder': 'Content', 'class': 'content-field'}),
        }