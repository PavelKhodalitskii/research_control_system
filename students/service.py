import json

from django.http import JsonResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from models_manager.models import (Account, 
                                   GraduateStudentProfile, 
                                   StudentProfile,
                                   StudentGroups,
                                   Speciality,
                                   Department,
                                   Faculty,
                                   Research)
from index.utils import MetaField

from .queries import (get_student_information_query_template,
                      get_student_information_by_id_query_template,
                      get_researches_by_account_id,
                      get_all_graduate_students_info,
                      get_graduate_student_by_id_query_template)



class StudentControllerBase:
    sql_fields = ["id", "accountid", "firstname", "lastname", "patronymic", "year", "studgroup", "speciality", "department", "faculty"]
    verbose_names = ["Id", "Id Аккаунта", "Имя", "Фамилия", "Отчество", "Курс", "Группа", "Специальность", "Кафедра", "Факультет"] 
    order_by_fields = ["id", "year"]
    foreign_key_fields = ["studgroup", "speciality", "department", "faculty"]
    foreign_key_choices = {
        "studgroup": StudentGroups.objects.all(),
        "speciality": Speciality.objects.all(),
        "department": Department.objects.all(),
        "faculty": Faculty.objects.all()
    }

    @classmethod
    def get_context_for_table_view(cls) -> dict:
        fields = []
        for i in range(len(cls.sql_fields)):
            fields.append(MetaField(cls.verbose_names[i], cls.sql_fields[i]))

        query = cls.all_objects_query_func()
        students = cls.model.objects.raw(query)

        return {
            "order_by_fields": cls.order_by_fields,
            "foreign_key_fields": cls.foreign_key_fields,
            "foreign_key_choices": cls.foreign_key_choices,
            
            "primary_key": "Id", 
            "fields": fields,
            "items": students
        }

    @classmethod
    def get_context_for_detail_view(cls, account_id: int) -> dict:
        query = cls.single_object_query_func(account_id)
        student = cls.model.objects.raw(query)[0]
        researches = StudentController.get_researches_by_acccount_id(account_id)
        return {
            "student": student,
            "researches": researches
        }

    @staticmethod
    def get_researches_by_acccount_id(account_id):
        query = get_researches_by_account_id(account_id)
        researches = Research.objects.raw(query)
        return researches

    @classmethod
    def delete_several_students(cls, request):
        data = json.loads(request.body.decode('utf-8'))
        pk_to_delete = data['delete']
        confirmed = bool(data['confirmed'])
        queryset = cls.model.objects.filter(pk__in = pk_to_delete)
        if not confirmed:
            return JsonResponse({"delete": [str(student) for student in queryset.all()]})
        else:
            queryset.delete()
            return JsonResponse({"status": "ok", 
                                "redirect": reverse_lazy('students_table')
                                })
        
    @classmethod    
    def delete_student(cls, request, account_id):
        student = cls.model.objects.filter(account__id=account_id)
        student.delete()
        return redirect('students_table')

class GraduateStudentController(StudentControllerBase):
    model = GraduateStudentProfile
    all_objects_query_func = get_all_graduate_students_info
    single_object_query_func = get_graduate_student_by_id_query_template

    @staticmethod
    def get_graduate_student_profile_by_account(account: Account) -> GraduateStudentProfile:
        profiles = GraduateStudentProfile.objects.filter(account__id = account.id)
        if profiles.exists():
            return profiles.first()
        return None

class StudentController(StudentControllerBase):
    model = StudentProfile
    all_objects_query_func = get_student_information_query_template
    single_object_query_func = get_student_information_by_id_query_template

    @staticmethod
    def get_student_profile_by_account(account: Account) -> StudentProfile:
        profiles = StudentProfile.objects.filter(account__id = account.id)
        if profiles.exists():
            return profiles.first()
        return None