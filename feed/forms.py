from django import forms
from .models import Comments, Post
from django.utils.translation import gettext_lazy as _


class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['description', 'pic', 'tags']


class NewCommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['comment']
