from models_manager.models import (Research, Event, Account, ResearchParticipants)
from teachers.service import TeacherController
from students.service import GraduateStudentController, StudentController

class ResearchesContorller:
    @staticmethod
    def get_researches_data(researches):
        researches_data = []
        for research in researches:
            researches_data.append({
                "research": research,
                "research_add_info": ResearchesContorller.get_research_information(research)
            })
        return researches_data

    @staticmethod
    def get_research_information(research: Research):
        committe_info = TeacherController.get_commitette_data(research.commitette)
        participants_accounts = ResearchesContorller.get_participants_accounts(research)
        participants_groups = {"participants": ResearchesContorller.get_user_grouped_by_account_cats(participants_accounts)}

        return committe_info | participants_groups

    @staticmethod
    def get_participants_accounts(research: Research) -> Account:
        accounts_ids = ResearchParticipants.objects.filter(research__id = research.id).values_list('account', flat=True)
        accounts = Account.objects.filter(id__in = accounts_ids).all()
        return accounts
    
    @staticmethod
    def get_user_grouped_by_account_cats(accounts: Account) -> dict:
        teachers = []
        students = []
        graduate_students = []

        for account in accounts:
            teacher = TeacherController.get_teacher_by_account(account)
            if teacher:
                teachers.append(teacher)
                continue
            student = StudentController.get_student_profile_by_account(account)
            if student:
                students.append(student)
                continue
            graduate_student = GraduateStudentController.get_graduate_student_profile_by_account(account)
            if graduate_student:
                graduate_students.append(graduate_student)
        
        return {
            "teachers": teachers,
            "students": students,
            "graduate_students": graduate_students
        }
            
