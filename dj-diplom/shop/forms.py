from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import CustomUser, Review

STAR_CHOICE = [
    ('1', '1'),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
    ("5", "5"),
]

class UserForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email',)

class ReviewForm(forms.ModelForm):
    stars = forms.IntegerField(widget=forms.RadioSelect(choices=STAR_CHOICE))

    class Meta:
        model = Review
        fields = ('stars', 'text')