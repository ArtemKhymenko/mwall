from django import forms
from .models import Comment, Post, CommentComment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

class CommentCommentForm(forms.ModelForm):
    class Meta:
        model = CommentComment
        fields = ('body',)

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)
