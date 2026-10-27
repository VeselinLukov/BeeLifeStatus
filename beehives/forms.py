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
            'beehive_description': forms.Textarea(attrs={'placeholder': 'Add description (optional)'})
        }

        error_messages = {
            'beehive_number': {
                'unique': 'Beehive number should be unique!',
            }
        }