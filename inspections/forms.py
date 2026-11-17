from django import forms

from inspections.models import Inspection


class InspectionsBaseForm(forms.ModelForm):
    class Meta:
        model = Inspection
        exclude = ['inspection_date']

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
                'placeholder': 'Add notes (if any) during the inspection',
            }),
            'beehive': forms.Select(),
        }


class InspectionCreateForm(InspectionsBaseForm):
    class Meta(InspectionsBaseForm.Meta):

        help_texts = {
            'colony_health': "Choose the colony health status",
            'queen_status': "Choose the queen status",
            'food_stores': "Add information about available food stores in the beehive",
            'inspection_notes': "Add notes (if any) during the inspection",
            'beehive': "Choose the beehive to which inspection should be recorded",
        }


class InspectionUpdateForm(InspectionsBaseForm):
    class Meta(InspectionsBaseForm.Meta):

        widgets = {
            'colony_health': forms.Select(),
            'queen_status': forms.Select(),
            'food_stores': forms.Textarea(attrs={
                'placeholder': 'Add information about food stores in the beehive',
            }),
            'inspection_notes': forms.Textarea(attrs={
                'placeholder': 'Add notes (if any) during the inspection',
            }),
            'beehive': forms.Select(),
        }

        help_texts = {
            'colony_health': "Choose the colony health status",
            'queen_status': "Choose the queen status",
            'food_stores': "Add information about available food stores in the beehive",
            'inspection_notes': "Add notes (if any) during the inspection",
            'beehive': "Choose the beehive to which inspection should be recorded",
        }
