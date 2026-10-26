from django import forms
from django.core.exceptions import ValidationError
from django.db.models.fields import URLField

from apiaries.models import Apiary


class ApiaryBaseForm(forms.ModelForm):
    class Meta:
        model = Apiary
        fields = ['name', 'location', 'number_of_hives', 'apiary_description',
                  'image_url']

        labels = {
            'name': "Apiary's name",
            'location': "Apiary's location",
            'number_of_hives': 'Number of hives',
            'apiary_description': 'Description',
            'image_url': 'Image URL'
        }

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Insert name'}),
            'location': forms.TextInput(attrs={'placeholder': 'Insert location'}),
            'number_of_hives': forms.TextInput(attrs={'placeholder': 'Insert number of hives'}),
            'apiary_description': forms.TextInput(attrs={'placeholder': 'Add description'}),
            'image_url': forms.TextInput(attrs={'placeholder': 'Insert image URL (optional)'})
        }

        def clean_location(self) -> str:
            location = self.cleaned_data["location"]

            if not location.isalpha():
                raise ValidationError("Location should contains only letters!")

            return location

        def clean_number_of_hives(self) -> int:
            number_of_hives = self.cleaned_data["number_of_hives"]

            if not number_of_hives.isdigit():
                raise ValidationError("Hives should be a number!")

            return number_of_hives


