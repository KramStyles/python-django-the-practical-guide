from django import forms

from challenges.models import Review


class BaseForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fields in self.visible_fields():
            fields.field.widget.attrs["class"] = "form-control my-1"


class ReviewForm(BaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fields in self.visible_fields():
            fields.field.widget.attrs["class"] = "form-control my-1"

    username = forms.CharField(
        max_length=100,
        required=True,
        label="User Name",
        error_messages={
            "required": "Username is important.",
            "max_length": "Maximum of 100 Characters exceeded.",
        },
    )
    review_text = forms.CharField(widget=forms.Textarea, required=False)
    ratings = forms.IntegerField(min_value=1, max_value=5, label="Your Ratings")


class ReviewModelForm(BaseForm, forms.ModelForm):
    class Meta:
        model = Review
        fields = "__all__"
        labels = {"ratings": "Your Rating"}
        error_messages = {
            "username": {
                "required": "Username is important.",
                "max_length": "Maximum of 100 Characters exceeded.",
            },
        }