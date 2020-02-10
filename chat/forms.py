from django import forms
from . models import Post, Comment




class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        exclude = ["user","created_on","updated_on"]


class CommentForm(forms.ModelForm):
    body = forms.CharField(required=False, label='', widget=forms.Textarea(attrs={'class':'form-control','rows': 1, 'cols': 5}))

    class Meta:
        model = Comment
        exclude = ["user","create","post"]
        
