from models_manager.models import (Account, GraduateStudentProfile, StudentProfile)


class GraduateStudentController:
    @staticmethod
    def get_graduate_student_profile_by_account(account: Account) -> GraduateStudentProfile:
        profiles = GraduateStudentProfile.objects.filter(account__id = account.id)
        if profiles.exists():
            return profiles.first()
        return None
    
class StudentController:
    @staticmethod
    def get_student_profile_by_account(account: Account) -> StudentProfile:
        profiles = StudentProfile.objects.filter(account__id = account.id)
        if profiles.exists():
            return profiles.first()
        return None