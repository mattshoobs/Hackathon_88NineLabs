from django.db import models

Class Incident(models.Model):
    incident.address_streeet=CharField(max_length=160)
    incident.address_city=CharField(max_length=20,Default='Milwaukee')
    incident.address_state=CharField(max_length=20,Default='Wisconsin')
    incident.address_zip=IntergerField(max_length=9)
    incident_time=TimeField()
    incident_date=DateField()
    subject_name=CharField(max_length=160)
    subject_badge_number=CharField(max_length=80)
    subject_car_number=CharField(max_length=80)
    subject_department=CharField(max_length=256)
    subject_physical_description=CharField(max_length=1000)
    incident_type=TextField()
    incident_was_ticketed=NullBooleanField()
    incident_has_warrent=NullBooleanField()
    indicent_was_searched=NullBooleanField()
    indicent_was_seized=NullBooleanField()
   	incident_was_detained=NullBooleanField()
   	indicent_was_concent=NullBooleanField()
   	indicent_details=TextField()
   	