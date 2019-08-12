from django import forms
from .models import Region, City

CHOICES = City.objects.filter(is_active=True)


class RegionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(RegionForm, self).__init__(*args, **kwargs)

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
        choices=((x.id, x.name) for x in CHOICES),
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
