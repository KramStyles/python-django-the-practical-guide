from django import forms


class ReviewForm(forms.Form):
    username = forms.CharField(max_length=100, required=True)
    password = forms.CharField(min_length=4, required=True)
