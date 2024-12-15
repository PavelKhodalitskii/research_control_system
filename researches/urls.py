from django.urls import path
from .views import EventListView, EventDetailView

urlpatterns = [
    path('', EventListView.as_view(), name="events_list"),
    path('event/details/<int:event_id>/', EventDetailView.as_view(), name="event_details")
]