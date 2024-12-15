from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from models_manager.models import Event

class ResearchesListView(ListView):
    model = Event
    template_name = 'researches/researches.html'
    context_object_name = 'events'