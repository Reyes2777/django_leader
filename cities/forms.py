from django import forms
from .models import Region, City


class RegionForm(forms.ModelForm):
    code = forms.CharField(
        widget=forms.TextInput()
    )
    name = forms.CharField(
        widget=forms.TextInput()
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
