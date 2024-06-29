from django import forms
from .models import climate

class climateform(forms.ModelForm):
    class Meta:
        model = climate
        fields = ('city', 'temperature', 'flood', 'wind_speed', 'carbon_emission', 'rainfall')