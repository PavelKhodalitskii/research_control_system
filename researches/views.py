from django.shortcuts import render
from django.views.generic import ListView, DetailView
from models_manager.models import Event, Research

from .service import ResearchesContorller

class EventListView(ListView):
    model = Event
    template_name = 'researches/researches.html'
    context_object_name = 'events'

class EventDetailView(DetailView):
    model = Event
    template_name = 'researches/event_details_view.html'
    context_object_name = 'event'
    pk_url_kwarg = 'event_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        event_id = self.kwargs['event_id']
        researches = Research.objects.filter(event__id=event_id).all()

        researches_data = []
        for research in researches:
            researches_data.append({
                "research": research,
                "research_add_info": ResearchesContorller.get_research_information(research)
            })

        # context['researches'] = Research.objects.filter(event__id=event_id).all()
        context['researches_data'] = researches_data
        return context
