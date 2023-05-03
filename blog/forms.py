from django import forms

from blog.models import Comment
from challenges.forms import BaseForm


class CommentForm(BaseForm, forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ["post", "created_on"]
        labels = {
            "user_name": "Full Name",
            "user_email": "Email Address",
            "text": "Comment"
        }
