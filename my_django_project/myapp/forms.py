from django import forms
from django.contrib.auth.models import User
from .models import Comment, Rank
import re

class UserRegistrationForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True, max_length=30)
    last_name = forms.CharField(required=True, max_length=30)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    confirm_password = forms.CharField(widget=forms.PasswordInput, required=True)
    country = forms.CharField(max_length=100, required=True)
    city = forms.CharField(max_length=100, required=True)

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'password', 'confirm_password', 'country', 'city']

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise forms.ValidationError('Password must be at least 8 characters long.')
        if not re.search(r'\d', password):
            raise forms.ValidationError('Password must contain at least one digit.')
        if not re.search(r'\W', password):
            raise forms.ValidationError('Password must contain at least one non-alphanumeric character.')
        return password

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            self.add_error('confirm_password', 'Passwords do not match.')
        return cleaned_data
    
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
        widgets = {
            'body': forms.Textarea(attrs={'rows': 3})
        }

class RankForm(forms.ModelForm):
    class Meta:
        model = Rank
        fields = ['score']
        widgets = {
            'score': forms.NumberInput(attrs={'min': 1, 'max': 10})
        }