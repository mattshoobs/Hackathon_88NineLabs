from django import forms
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Incident


class IncidentForm(ModelForm):
    incident_address_street=forms.CharField(max_length=160, label="Street Address")
    incident_address_city=forms.CharField(max_length=20, label="City")
    incident_address_state=forms.CharField(max_length=20, label="State")
    incident_address_zip=forms.CharField(max_length=10, label="Zip Code")
    incident_time=forms.TimeField(label="Time of Incident")
    incident_date=forms.DateField(label="Date of Incident")
    subject_name=forms.CharField(max_length=160, required=False, label="Name of Official")
    subject_badge_number=forms.CharField(max_length=80, required=False, label="Badge Number")
    subject_car_number=forms.CharField(max_length=80, required=False, label="Vehicle Number")
    subject_department=forms.CharField(max_length=256, label="Police Department or Fire Department")
    subject_physical_description=forms.CharField(max_length=1000, label="Describe what the official looked like.")
    incident_type=forms.TextInput()
    incident_was_ticketed=forms.NullBooleanField(label="Did you receive a ticket?")
    incident_has_warrent=forms.NullBooleanField(required=False, label="To your knowledge, Did they had a warrant?")
    indicent_was_searched=forms.NullBooleanField(required=False, label="Were you searched?")
    indicent_was_seized=forms.NullBooleanField(required=False, label="Were any of your possessions seized?")
    incident_was_detained=forms.NullBooleanField(required=False, label="Were you detained?")
    indicent_was_concent=forms.NullBooleanField(required=False, label="Did you give consent?")
    indicent_details=forms.TextInput()

    class Meta:
        model = Incident
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(IncidentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)

        self.helper.add_input(Submit('submit', 'File Complaint'))
