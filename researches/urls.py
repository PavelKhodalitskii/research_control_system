from django.urls import path
from .views import ResearchesListView

urlpatterns = [
    path('', ResearchesListView.as_view(), name="researches"),
]