from django import forms
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Incident


class IncidentForm(ModelForm):
    INCIDENT_TYPE_CHOICES=(('physical_abuse','Physical Abuse'),
                           ('verbal_abuse','Verbal Abuse'),
                           ('false_detainment','False Detainment'),
                           ('improper_search','Improper Search'),
                           ('racial_profiling','Racial Profiling'),
                           ('sexual_harassment','Sexual Harassment'),
                           ('unwarranted_surveillance','Unwarranted Surveillance'),
                           ('intimidation','Intimidation'),
                           ('false_evidence','False/Tampering with Evidence'))

    DEPARTMENT_CHOICES = (('fire', 'Fire Department',), ('police', 'Police Department',))

    incident_address_street=forms.CharField(max_length=160, label="Street Address")
    incident_address_city=forms.CharField(max_length=20, label="City", initial="Milwaukee")
    incident_address_state=forms.CharField(max_length=20, label="State", initial="Wisconsin")
    incident_address_zip=forms.CharField(max_length=10, label="Zip Code")
    incident_time=forms.TimeField(label="Time of Incident", help_text="HH:MM")
    incident_date=forms.DateField(label="Date of Incident", help_text="MM/DD/YYYY", widget=forms.DateInput)
    incident_type=forms.MultipleChoiceField(label="Incident Type", widget=forms.CheckboxSelectMultiple, choices=INCIDENT_TYPE_CHOICES)
    subject_name=forms.CharField(max_length=160, required=False, label="Name of Official")
    subject_badge_number=forms.CharField(max_length=80, required=False, label="Badge Number")
    subject_car_number=forms.CharField(max_length=80, required=False, label="Vehicle Number")
    subject_department=forms.ChoiceField(label="Police Department or Fire Department", help_text="Fire or Police", widget=forms.RadioSelect, choices=DEPARTMENT_CHOICES)
    subject_physical_description=forms.CharField(max_length=1000, label="Describe what the official looked like.")
    incident_was_ticketed=forms.NullBooleanField(required=False, label="Did you receive a ticket?", widget=forms.CheckboxInput)
    incident_has_warrent=forms.NullBooleanField(required=False, label="To your knowledge, Did they had a warrant?", widget=forms.CheckboxInput)
    indicent_was_searched=forms.NullBooleanField(required=False, label="Were you searched?", widget=forms.CheckboxInput)
    indicent_was_seized=forms.NullBooleanField(required=False, label="Were any of your possessions seized?", widget=forms.CheckboxInput)
    incident_was_detained=forms.NullBooleanField(required=False, label="Were you detained?", widget=forms.CheckboxInput)
    indicent_was_concent=forms.NullBooleanField(required=False, label="Did you give consent?", widget=forms.CheckboxInput)
    indicent_details=forms.TextInput()



    class Meta:
        model = Incident
        fields = [
            'incident_address_street',
            'incident_address_city',
            'incident_address_state',
            'incident_address_zip',
            'incident_time',
            'incident_date',
            'incident_type',
            'subject_name',
            'subject_badge_number',
            'subject_car_number',
            'subject_department',
            'subject_physical_description',
            'incident_was_ticketed',
            'incident_has_warrent',
            'indicent_was_searched',
            'indicent_was_seized',
            'incident_was_detained',
            'indicent_was_concent']


    def __init__(self, *args, **kwargs):
        super(IncidentForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        self.helper.add_input(Submit('submit', 'File Complaint'))
