from django import forms
from .models import Region, City


class RegionForm(forms.ModelForm):

    code = forms.CharField(
        required=True,
        widget=forms.TextInput(),
        label='Código',

    )
    name = forms.CharField(
        required=True,
        widget=forms.TextInput(),
        label='Nombre'
    )
    cities = forms.MultipleChoiceField(
        required=False,
        label='Ciudades',
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Region
        fields = ['code', 'name', 'cities']
        widgets = {
            'name': forms.Textarea(),
            'cities': forms.CheckboxSelectMultiple()
        }


class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ['code', 'name', 'is_active']
