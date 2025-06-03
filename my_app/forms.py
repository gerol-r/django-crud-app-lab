from django import forms
from .models import Review
from datetime import date

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'opinion', 'date_watched']
        widgets = {
            'date_watched': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={
                    'placeholder': 'Select a date',
                    'type': 'date',
                    'value': date.today().strftime('%Y-%m-%d')  # Default to today
                }
            ),
            'opinion': forms.Textarea(attrs={'rows': 3}),
        }