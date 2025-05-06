from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# User registration form
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    preferred_categories = forms.CharField(
        required=True,
        max_length=255,
        help_text="Enter at least 3 topics separated by commas (e.g., technology, sports, health)",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Required (e.g. technology, sports, health)'
        })
    )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'preferred_categories', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        for fieldname in self.fields:
            if fieldname != 'preferred_categories':  # Because preferred_categories already has its own widget
                self.fields[fieldname].widget.attrs.update({'class': 'form-control'})

    def clean_preferred_categories(self):
        data = self.cleaned_data.get('preferred_categories')
        topics = [t.strip() for t in data.split(',') if t.strip()]
        if len(topics) < 3:
            raise forms.ValidationError("Please enter at least 3 topics separated by commas.")
        return ', '.join(topics)  # Store as clean comma-separated string

# Feedback form
class FeedbackForm(forms.Form):
    feedback = forms.CharField(
        label='Your Feedback',
        widget=forms.Textarea(attrs={
            'rows': 4,
            'class': 'form-control',
            'placeholder': 'Tell us what you think...'
        }),
        max_length=1000
    )
