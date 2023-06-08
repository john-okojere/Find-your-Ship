from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ('A_picture_of_Daddie', 'Your_story')