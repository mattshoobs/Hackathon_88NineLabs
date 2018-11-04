from django.shortcuts import render
from django.views.generic import CreateView
from .models import Incident
from .forms import IncidentForm

class IncidentCreate(CreateView):
    template_name = 'incident_report.html'
    model = Incident
    form_class = IncidentForm

    def get_context_data(self, **kwargs):
        context = super(IncidentCreate, self).get_context_data(**kwargs)
        context['page_title'] = 'Report Abuse'
        return context
