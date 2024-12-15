from models_manager.models import (Commitette, 
                                   Account,
                                   TeacherProfile)

class TeachersController:
    @staticmethod
    def get_commitette_data(commitette: Commitette) -> dict:
        chairman = commitette.chairman
        participants_accounts = TeachersController.get_commitette_participants(commitette)
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

