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
        print(f'TEST STUFF ***** {self.incident_address_city}')
        # Put all business logic for sending the fields and calling the old form here.
