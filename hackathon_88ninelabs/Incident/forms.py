from django import forms
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Incident


class IncidentForm(ModelForm):
    incident_address_street=forms.CharField(max_length=160)
    incident_address_city=forms.CharField(max_length=20 )
    incident_address_state=forms.CharField(max_length=20)
    incident_address_zip=forms.IntegerField()
    incident_time=forms.TimeField()
    incident_date=forms.DateField()
    subject_name=forms.CharField(max_length=160)
    subject_badge_number=forms.CharField(max_length=80)
    subject_car_number=forms.CharField(max_length=80)
    subject_department=forms.CharField(max_length=256)
    subject_physical_description=forms.CharField(max_length=1000)
    incident_type=forms.TextInput()
    incident_was_ticketed=forms.NullBooleanField()
    incident_has_warrent=forms.NullBooleanField()
    indicent_was_searched=forms.NullBooleanField()
    indicent_was_seized=forms.NullBooleanField()
    incident_was_detained=forms.NullBooleanField()
    indicent_was_concent=forms.NullBooleanField()
    indicent_details=forms.TextInput()
    class Meta:
        model = Incident
        fields = '__all__'
