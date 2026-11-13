from django import forms

from inspections.models import Inspection


class InspectionsBaseForm(forms.ModelForm):
    class Meta:
        model = Inspection

        labels = {
            'colony_health': "Colony health",
            'queen_status': "Queen status",
            'food_stores': "Food stores",
            'inspection_notes': "Inspection notes",
            'beehive': "Beehive",
        }

        widgets = {
            'colony_health': forms.Select(),
            'queen_status': forms.Select(),
            'food_stores': forms.Textarea(attrs={
                'placeholder': 'Add information about food stores in the beehive',
            }),
            'inspection_notes': forms.Textarea(attrs={
                'placeholder': 'Add notes during the inspection',
            }),
        }
