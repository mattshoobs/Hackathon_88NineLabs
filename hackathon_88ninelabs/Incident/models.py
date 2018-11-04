from django.db import models

class Incident(models.Model):
    AVAILABLE_DEPARTMENTS = (('Fire','Fire Department'),('Police', 'Police Department'))

    incident_address_street=models.CharField(max_length=160)
    incident_address_city=models.CharField(max_length=20,default='Milwaukee')
    incident_address_state=models.CharField(max_length=20,default='Wisconsin')
    incident_address_zip=models.IntegerField()
    incident_time=models.TimeField()
    incident_date=models.DateField()
    subject_name=models.CharField(max_length=160)
    subject_badge_number=models.CharField(max_length=80)
    subject_car_number=models.CharField(max_length=80)
    subject_department=models.CharField(max_length=256, choices=AVAILABLE_DEPARTMENTS)
    subject_physical_description=models.CharField(max_length=1000)
    incident_type=models.TextField()
    incident_was_ticketed=models.NullBooleanField()
    incident_has_warrent=models.NullBooleanField()
    indicent_was_searched=models.NullBooleanField()
    indicent_was_seized=models.NullBooleanField()
    incident_was_detained=models.NullBooleanField()
    indicent_was_concent=models.NullBooleanField()
    indicent_details=models.TextField()

    def save(self, *args, **kwargs):
        cmsForm_Incident_Location = f'{self.incident_address_street} {self.incident_address_city} {self.incident_address_state}, {self.incident_address_zip}'
        cmsForm_Date_of_incident = f'{self.incident_date}'
        cmsForm_incident_time = f'{self.incident_time}'
        cmsForm_AM_PM = f'PM'
        cmsForm_Department = f'{self.subject_department}'
        cmsForm_name_or_description_of_employee = f'Name: {self.subject_name}' \
                                                  f'\n Badge Number: {self.subject_badge_number}' \
                                                  f'\n Car Number: {self.subject_car_number}' \
                                                  f'\n Physical Description: {self.subject_physical_description}'
        cmsForm_incident_description = f'Incident Type: {self.incident_type}' \
                                       f'\n Ticketed? {self.incident_was_ticketed}' \
                                       f'\n Detained? {self.incident_was_detained}' \
                                       f'\n Warrent? {self.incident_has_warrent}' \
                                       f'\n Searched? {self.indicent_was_searched}' \
                                       f'\n Seized? {self.indicent_was_seized}' \
                                       f'\n Gave concent? {self.indicent_was_concent}' \
                                       f'\n Other details: {self.indicent_details}'
        cmsForm_desired_outcome = f'TODO: ADD DESIRED OUTCOME FIELD'
        print(f'\n ************** DATA DUMP TO LIVE FORM OR API ***********************'
              f'\n {cmsForm_Incident_Location}'
              f'\n {cmsForm_Date_of_incident}'
              f'\n {cmsForm_incident_time} {cmsForm_AM_PM}'
              f'\n {cmsForm_Department}'
              f'\n {cmsForm_name_or_description_of_employee}'
              f'\n {cmsForm_incident_description}'
              f'\n {cmsForm_desired_outcome}')
        # Put all business logic for sending the fields and calling the old form here.
