from django import forms

from beehives.models import Beehive


class BeehiveBaseForm(forms.ModelForm):
    class Meta:
        model = Beehive
        exclude = ['installation_date']

        labels = {
            'beehive_number': "Beehive number",
            'beehive_type': "Beehive type",
            'current_status': 'Current status',
            'beehive_description': 'Description',
            'apiary': 'Apiary',
        }

        widgets = {
            'beehive_number': forms.NumberInput(attrs={'placeholder': 'Insert number'}),
            'beehive_type': forms.Select(),
            'current_status': forms.Select(),
            'beehive_description': forms.Textarea(
                attrs={
                    'placeholder': 'Add description (optional)'
                }),
            'apiary': forms.Select(),
        }

        error_messages = {
            'beehive_number': {
                'unique': 'Beehive number should be unique!',
            }
        }


class BeehiveCreateForm(BeehiveBaseForm):
    class Meta(BeehiveBaseForm.Meta):
        help_texts = {
            'beehive_number': "Number should be unique. ",
            'beehive_type': "Select your type of beehive structure.",
            'current_status': "Select your current status of the colony.",
            'beehive_description': "Optional. Add any description.",
            'apiary': "Choose to which apiary belongs the beehive.",
        }


class BeehiveUpdateForm(BeehiveBaseForm):
    class Meta(BeehiveBaseForm.Meta):
        widgets = {
            'beehive_number': forms.NumberInput(
                attrs={
                    'placeholder': 'Insert number',
                    'disabled': 'disabled',
                }),
            'beehive_type': forms.Select(),
            'current_status': forms.Select(),
            'beehive_description': forms.Textarea(
                attrs={
                    'placeholder': 'Add description (optional)'
                }),
        }

        help_texts = {
            'beehive_number': "You can't change your beehive number. ",
            'beehive_type': "Select your type of beehive structure.",
            'current_status': "Select your current status of the colony.",
            'beehive_description': "Optional. Add any description.",
            'apiary': "Choose to which apiary belongs the beehive.",
        }
