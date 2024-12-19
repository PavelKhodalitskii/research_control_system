from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, FormView
from models_manager.models import Event, Research, Faculty

from .service import ResearchesContorller
from .forms import ResearchCreationForm

class ResearchCreateView(FormView):
    template_name = 'researches/create_research_view.html'
    form_class = ResearchCreationForm
    success_url = "/"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['success_url'] = 'events_list'
        return context

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class EventListView(ListView):
    model = Event
    template_name = 'researches/researches.html'
    context_object_name = 'events'
    foreign_key_fields = ['']
    order_by_fields = ['date']

    def filter_raw_data(self, queryset):
        for field in self.foreign_key_fields:
            filter_value = self.request.GET.get(field)
            if filter_value:
                filtered_items = []
                for item in queryset:
                    if str(item.__getattribute__(field)) == str(queryset[field].filter(pk=filter_value).first()):
                        filtered_items.append(item)
                queryset = filtered_items

        for field in self.order_by_fields:
            filter_value = self.request.GET.get(field)
            if filter_value == 'ascending':
                queryset = sorted(queryset, key=lambda x: x.__getattribute__(field), reverse=False)
            elif filter_value == 'descending':
                queryset= sorted(queryset, key=lambda x: x.__getattribute__(field), reverse=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['faculties'] = Faculty.objects.all()
        return context

    def get_queryset(self):
        queryset = super().get_queryset()

        year_filter = self.request.GET.get('year')
        if year_filter:
            queryset = queryset.filter(date__year=year_filter)

        date_filter = self.request.GET.get('date')
        if date_filter:
            queryset = queryset.filter(date=date_filter)

        faculty_id = self.request.GET.get('faculty')
        if faculty_id:
            queryset = queryset.filter(faculty__id=faculty_id)

        return queryset

class EventDetailView(DetailView):
    model = Event
    template_name = 'researches/event_details_view.html'
    context_object_name = 'event'
    pk_url_kwarg = 'event_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        event_id = self.kwargs['event_id']
        researches = Research.objects.filter(event__id=event_id).all()

        researches_data = ResearchesContorller.get_researches_data(researches)
        context['researches_data'] = researches_data
        return context

class ResearchDetailView(DetailView):
    model = Research
    template_name = 'researches/research_details_view.html'
    pk_url_kwarg = 'research_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        research_id = self.kwargs['research_id']
        research = get_object_or_404(Research, pk=research_id)

        research_data = {
            "research": research,
            "research_add_info": ResearchesContorller.get_research_information(research)
        }

        context["research_data"] = research_data
        return context