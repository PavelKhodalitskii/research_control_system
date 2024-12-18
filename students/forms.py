from django import forms
from django.db import models
from models_manager.models import StudentGroups, StudentProfile, Account

class StudentCreationForm(forms.Form):
    first_name = forms.CharField(max_length=48, label="Имя")
    last_name = forms.CharField(max_length=48, label="Фамилия")
    patronymic = forms.CharField(max_length=48, required=False, label="Отчество")
    group = forms.ModelChoiceField(StudentGroups.objects.all(), required=True, label='Группа')
    year = forms.IntegerField(min_value=1, max_value=6, required=True, label='Курс')

    def save(self):
        cleaned_data = self.cleaned_data
        result = Account.objects.raw(f"select * from create_account('{cleaned_data['first_name']}', '{cleaned_data['last_name']}', '{cleaned_data['patronymic']}')")
        print(result[0].accountid)
        StudentProfile.objects.raw(f"select * from create_student({result[0].id}, {cleaned_data['group']}, {cleaned_data['year']})")