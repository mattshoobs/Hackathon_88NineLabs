from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import Incident
from .forms import IncidentForm

class IncidentCreate(CreateView):
    template_name = 'forms/crispy_incident_report_form.html'
    model = Incident
    form_class = IncidentForm
    success_msg = "Complaint Filed Successfully!"

    def get_success_url(self, **kwargs):
        return reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super(IncidentCreate, self).get_context_data(**kwargs)
        context['page_title'] = 'Report Abuse'
        return context
