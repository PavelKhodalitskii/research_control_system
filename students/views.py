import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView

from researches.service import ResearchesContorller

from .service import StudentController, GraduateStudentController
from .forms import StudentCreationForm, GraduateCreationForm

from index.utils import get_table_data_by_model
from index.views import TableRawDataView

from models_manager.models import StudentProfile, GraduateStudentProfile


class CreateStudentView(FormView):
    template_name = "index/includes/form.html"
    form_class = StudentCreationForm
    success_url = "/students/table/"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['success_url'] = 'students_table'
        return context

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class StudentTableView(TableRawDataView):
    template_name = 'students/students_main_view.html'
    title = 'Таблица студентов'
    table_url = 'students_table'
    creation_form_url = 'create_student'
    delete_several_url = 'delete_several_students'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        addition = StudentController.get_context_for_table_view()
        self.filter_raw_data(addition)
        context = context | addition
        return context

class StudentDetailView(TemplateView):
    template_name = 'students/student_detail_view.html'
    title = 'Подробная информация о студенте'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        account_id = self.kwargs['account_id']
        addition = StudentController.get_context_for_detail_view(account_id)
        context = context | addition

        context["title"] = self.title

        researches_data = ResearchesContorller.get_researches_data(context["researches"])
        context['researches_data'] = researches_data

        return context

def delete_several_students(request):
    data = json.loads(request.body.decode('utf-8'))
    pk_to_delete = data['delete']
    confirmed = bool(data['confirmed'])
    queryset = StudentProfile.objects.filter(pk__in = pk_to_delete)
    if not confirmed:
        return JsonResponse({"delete": [str(student) for student in queryset.all()]})
    else:
        queryset.delete()
        return JsonResponse({"status": "ok", 
                             "redirect": reverse_lazy('students_table')
                            })
    
def delete_student(request, student_id):
    student = StudentProfile.objects.filter(id=student_id)
    student.delete()
    return redirect('students_table')

####

class GraduatesCreateView(FormView):
    template_name = "index/includes/form.html"
    form_class = GraduateCreationForm
    success_url = "/students/graduates/table/"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['success_url'] = 'graduates_table'
        return context

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class GraduatesTableView(TableRawDataView):
    template_name = 'students/students_main_view.html'
    title = 'Таблица аспирантов'
    table_url = 'graduates_table'
    creation_form_url = 'create_graduate'
    delete_several_url = 'delete_several_graduates'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        addition = GraduateStudentController.get_context_for_table_view()
        self.filter_raw_data(addition)
        context = context | addition
        return context

class GraduateDetailView(TemplateView):
    template_name = 'students/student_detail_view.html'
    title = 'Подробная информация о студенте'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        account_id = self.kwargs['account_id']
        addition = GraduateStudentController.get_context_for_detail_view(account_id)
        context = context | addition

        context["title"] = self.title

        researches_data = ResearchesContorller.get_researches_data(context["researches"])
        context['researches_data'] = researches_data

        return context