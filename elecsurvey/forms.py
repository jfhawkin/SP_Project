from django import forms
from elecsurvey.models import Factor

FACTOR_CHOICES = (
    (1, "Utility Cost"),
    (2, "Emissions"),
    (3, "Distance"),
    (4, "Research Cost"),
    (5, "Other"),
)

class FactorForm(forms.ModelForm):
    fact1 = forms.CharField(max_length=25,help_text="(e.g. utility cost, emissions, distance, research cost)", required=True)
    class Meta:
        model=Factor
        fields = '__all__'