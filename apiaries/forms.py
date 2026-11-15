from django import forms
from django.core.exceptions import ValidationError

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
            'number_of_hives': forms.NumberInput(attrs={'placeholder': 'Insert number of hives'}),
            'apiary_description': forms.TextInput(attrs={'placeholder': 'Add description'}),
            'image_url': forms.URLInput(attrs={'placeholder': 'Insert image URL (optional)'})
        }

    def clean_location(self) -> str:
        location = self.cleaned_data["location"]

        if not location.replace(' ', '').isalpha():
            raise ValidationError("Location should contains only letters!")

        return location

    def clean_number_of_hives(self) -> int:
        number_of_hives = self.cleaned_data["number_of_hives"]

        if number_of_hives < 0:
            raise ValidationError("Hives should be a positive number!")

        return number_of_hives


class ApiaryCreateForm(ApiaryBaseForm):
    class Meta(ApiaryBaseForm.Meta):
        help_texts = {
            'name': "Minimum 5 characters (letters and numbers). Name should be unique.",
            'location': "Add area's name, where the apiary is created.",
            'number_of_hives': 'Add how many beehives are (if any). Default is 0.',
            'apiary_description': 'Optional. Example description: type of honey, area'
                                  'specifications, etc. ',
            'image_url': 'Optional. Add direct URL to your apiary photo.'
        }


class ApiaryUpdateForm(ApiaryBaseForm):
    class Meta(ApiaryBaseForm.Meta):

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Insert name',
                    'disabled': 'disabled',
                }),
            'location': forms.TextInput(attrs={'placeholder': 'Insert location'}),
            'number_of_hives': forms.NumberInput(attrs={'placeholder': 'Insert number of hives'}),
            'apiary_description': forms.TextInput(attrs={'placeholder': 'Add description'}),
            'image_url': forms.URLInput(attrs={'placeholder': 'Insert image URL (optional)'}),
        }

        help_texts = {
            'name': "You can't edit your apiary name.",
            'location': "Add area's name, where the apiary is created.",
            'number_of_hives': 'Add how many beehives are (if any). Default is 0.',
            'apiary_description': 'Optional. Example description: type of honey, area'
                                  'specifications, etc. ',
            'image_url': 'Optional. Add direct URL to your apiary photo.',
        }
