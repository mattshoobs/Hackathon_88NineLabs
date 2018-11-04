from django.urls import path
from .views import (IncidentCreate)

app_name = 'incident'
urlpatterns = [
    path('report-incident', IncidentCreate.as_view(), name='incident_create'),
]
