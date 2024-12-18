import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView

from .service import TeacherController
from .forms import TeacherCreationForm

from index.utils import get_table_data_by_model
from index.views import TableRawDataView

from models_manager.models import StudentProfile, TeacherProfile

class CreateTeacherView(FormView):
    template_name = "index/includes/form.html"
    form_class = TeacherCreationForm
    success_url = "/teachers/table/"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['success_url'] = 'teachers_table'
        return context

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class TeacherTableView(TableRawDataView):
    template_name = 'teachers/teachers_table_view.html'
    title = 'Таблица преподавателей'
    table_url = 'teachers_table'
    creation_form_url = 'create_teacher'
    delete_several_url = 'delete_several_teachers'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        addition = TeacherController.get_context_for_table_view()
        self.filter_raw_data(addition)
        context = context | addition
        return context
    
class TeacherDetailView(TemplateView):
    template_name = 'teachers/teacher_detail_view.html'
    title = 'Подробная информация о преподавателе'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        account_id = self.kwargs['account_id']
        addition = TeacherController.get_context_for_detail_view(account_id)
        context = context | addition
        context["title"] = self.title
        return context

def delete_several_teachers(request):
    data = json.loads(request.body.decode('utf-8'))
    pk_to_delete = data['delete']
    confirmed = bool(data['confirmed'])
    queryset = TeacherProfile.objects.filter(pk__in = pk_to_delete)
    if not confirmed:
        return JsonResponse({"delete": [str(teacher) for teacher in queryset.all()]})
    else:
        queryset.delete()
        return JsonResponse({"status": "ok", 
                             "redirect": reverse_lazy('teachers_table')
                            })
    
def delete_teacher(request, account_id):
    teacher = TeacherProfile.objects.filter(id=account_id)
    teacher.delete()
    return redirect('teachers_table')