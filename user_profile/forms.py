from django import forms

from challenges.forms import BaseForm
from user_profile.models import UserProfile


class ProfileForm(BaseForm):
    user_image = forms.FileField(
        label="Upload File", error_messages={"required": "This shouldn't be omitted"}
    )


class ModelProfileForm(BaseForm, forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = "__all__"
        labels = {"cv": "Curriculum Vitae", "image": "Profile Picture"}
        error_messages = {
            "cv": {
                "required": "This is important",
            },
            "image": {
                "required": "We need your Image too",
            },
        }
