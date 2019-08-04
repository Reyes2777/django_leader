from django import forms
from .models import Region, City


class RegionForm(forms.ModelForm):
    class Meta:
        model = Region
        fields = ['code', 'name']


class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ['code', 'name', 'is_active']
