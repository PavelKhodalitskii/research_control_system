from models_manager.models import (Commitette, 
                                   Account,
                                   TeacherProfile, 
                                   Post,
                                   AcademicDegree,
                                   Department)

from index.utils import MetaField
from .queries import (get_teachers_information_query_template,
                      get_teacher_information_by_id_query_template)

class TeacherController:
    @staticmethod
    def get_context_for_detail_view(account_id: int) -> dict:
        query = get_teacher_information_by_id_query_template(account_id)
        teacher = TeacherProfile.objects.raw(query)[0]
        return {
            "teacher": teacher
        }

    @staticmethod
    def get_context_for_table_view() -> dict:
        sql_fields = ["id", "accountid", "firstname", "lastname", "patronymic", "post", "degree", "department", "ishead"]
        verbose_names = ["Id", "Id Аккаунта", "Имя", "Фамилия", "Отчество", "Должность", "Научная степень", "Кафедра", "Глава"]
        
        order_by_fields = ["id", "ishead"]

        foreign_key_fields = ["post", "degree", "department"]
        foreign_key_choices = {
            "post": Post.objects.all(),
            "degree": AcademicDegree.objects.all(),
            "department": Department.objects.all(),
        }

        fields = []
        for i in range(len(sql_fields)):
            fields.append(MetaField(verbose_names[i], sql_fields[i]))
        query = get_teachers_information_query_template()
        students = TeacherProfile.objects.raw(query)

        return {
            "order_by_fields": order_by_fields,
            "foreign_key_fields": foreign_key_fields,
            "foreign_key_choices": foreign_key_choices,
            
            "primary_key": "Id", 
            "fields": fields,
            "items": students
        }

    @staticmethod
    def get_commitette_data(commitette: Commitette) -> dict:
        chairman = commitette.chairman
        participants_accounts = TeacherController.get_commitette_participants(commitette)
        return {"chairman": chairman,
                "committe_participants_accounts": participants_accounts}

    @staticmethod
    def get_commitette_participants(commitette: Commitette) -> Account:
        pass

    @staticmethod
    def get_teacher_by_account(account: Account) -> TeacherProfile:
        profiles = TeacherProfile.objects.filter(account__id = account.id)
        if profiles.exists():
            return profiles.first()
        return None

