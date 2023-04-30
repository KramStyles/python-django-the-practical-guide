from django import forms


class ReviewForm(forms.Form):
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
    password = forms.CharField(min_length=4, required=True)
    review_text = forms.CharField(widget=forms.Textarea, required=False)
    ratings = forms.IntegerField(min_value=1, max_value=5, label="Your Ratings")
