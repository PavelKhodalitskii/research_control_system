from django.urls import path
from .views import EventListView, EventDetailView, ResearchDetailView

urlpatterns = [
    path('', EventListView.as_view(), name="events_list"),
    path('event/details/<int:event_id>/', EventDetailView.as_view(), name="event_details"),
    path('research/details/<int:research_id>/', ResearchDetailView.as_view(), name="research_details")
]