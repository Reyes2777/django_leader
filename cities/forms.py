from django import forms
from .models import Region, City

CHOICES = City.objects.filter(is_active=True)


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
    
    cities = forms.ModelMultipleChoiceField(
            widget=forms.CheckboxSelectMultiple,
            required=False
    )

    class Meta:
        model = Region
        fields = ['code', 'name', 'cities']
        widgets = {
            'name': forms.Textarea(),
        }


class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ['code', 'name', 'is_active']
