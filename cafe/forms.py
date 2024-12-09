from django import forms
from .models import FlavorSuggestion, Allergen

class FlavorSuggestionForm(forms.ModelForm):
    class Meta:
        model = FlavorSuggestion
        fields = ['name', 'description', 'allergens']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }

class AllergenForm(forms.ModelForm):
    class Meta:
        model = Allergen
        fields = ['name', 'description'] 