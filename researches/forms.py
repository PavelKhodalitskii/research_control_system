from django import forms
from django.db import models
from models_manager.models import StudentGroups, StudentProfile, Account, Faculty, TeacherProfile

class ResearchCreationForm(forms.Form):
    event_name = forms.CharField(max_length=1024, required=True, label="Название мероприятия")
    event_type = forms.CharField(max_length=1024, required=True, label="Тип мероприятия")
    city = forms.CharField(max_length=256, required=True, label="Город")
    street = forms.CharField(max_length=256, required=True, label='Улица')
    number = forms.CharField(max_length=256, required=True, label='Номер')
    date = forms.DateField(required=False)
    faculty = forms.ModelChoiceField(Faculty.objects.all(), required=True, label='Факультет')
    ###
    committe_chairman = forms.ModelChoiceField(TeacherProfile.objects.all(), required=True, label='Председатель коммитета')
    committe_participants = forms.ModelMultipleChoiceField(Account.objects.all(), label="Участники коммитета")

    def save(self):
        cleaned_data = self.cleaned_data
        result = Account.objects.raw(f"select * from create_account('{cleaned_data['first_name']}', '{cleaned_data['last_name']}', '{cleaned_data['patronymic']}')")
        print(result[0].accountid)
        StudentProfile.objects.raw(f"select * from create_student({result[0].id}, {cleaned_data['group']}, {cleaned_data['year']})")