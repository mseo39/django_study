from django import forms
from .models import Blog

class BlogPost(forms.ModelForm):
    class Meta: #meta라고 쓰면 오류,,,
        model = Blog
        fields = ['title','body']