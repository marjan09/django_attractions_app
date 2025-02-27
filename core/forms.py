from django import forms
from django.contrib.auth.models import User
from .models import Comment
import re
class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password"]

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        # Password and confirm_password matching check
        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")

        # Password strength validation
        if password:
            # Password length check
            if len(password) < 8:
                raise forms.ValidationError('Password must be at least 8 characters long.')

            # Password must contain at least one uppercase letter
            if not re.search(r'[A-Z]', password):
                raise forms.ValidationError('Password must contain at least one uppercase letter.')

            # Password must contain at least one lowercase letter
            if not re.search(r'[a-z]', password):
                raise forms.ValidationError('Password must contain at least one lowercase letter.')

            # Password must contain at least one number
            if not re.search(r'[0-9]', password):
                raise forms.ValidationError('Password must contain at least one number.')

            # Password must contain at least one special character
            if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
                raise forms.ValidationError('Password must contain at least one special character.')

        return cleaned_data


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]