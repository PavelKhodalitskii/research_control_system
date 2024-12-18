from models_manager.models import (Account, 
                                   GraduateStudentProfile, 
                                   StudentProfile,
                                   StudentGroups,
                                   Speciality,
                                   Department,
                                   Faculty)
from index.dataloader import DataLoader
from .queries import (get_student_information_query_template,
                      get_student_information_by_id_query_template)

class GraduateStudentController:
    @staticmethod
    def get_graduate_student_profile_by_account(account: Account) -> GraduateStudentProfile:
        profiles = GraduateStudentProfile.objects.filter(account__id = account.id)
        if profiles.exists():
            return profiles.first()
        return None
    
class SQLToDjangoField:
    def __init__(self, verbose_name, name):
        self.verbose_name = verbose_name
        self.name = name

class StudentController:
    @staticmethod
    def get_context_for_table_view() -> dict:
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

        fields = []
        for i in range(len(sql_fields)):
            fields.append(SQLToDjangoField(verbose_names[i], sql_fields[i]))
        query = get_student_information_query_template()
        students = StudentProfile.objects.raw(query)
        return {
            "order_by_fields": order_by_fields,
            "foreign_key_fields": foreign_key_fields,
            "foreign_key_choices": foreign_key_choices,
            
            "primary_key": "Id", 
            "fields": fields,
            "items": students
        }

    @staticmethod
    def get_context_for_detail_view(student_id: int) -> dict:
        # sql_fields = ["id", "accountid", "firstname", "lastname", "patronymic", "year", "studgroup", "speciality", "department", "faculty"]
        query = get_student_information_by_id_query_template(student_id)
        student = StudentProfile.objects.raw(query)[0]
        return {
            "student": student
        }

    @staticmethod
    def get_student_profile_by_account(account: Account) -> StudentProfile:
        profiles = StudentProfile.objects.filter(account__id = account.id)
        if profiles.exists():
            return profiles.first()
        return None