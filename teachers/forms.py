from django import forms
from django.db import models
from models_manager.models import Post, AcademicDegree, Department

class TeacherCreationForm(forms.Form):
    first_name = forms.CharField(max_length=48, label="Имя")
    last_name = forms.CharField(max_length=48, label="Фамилия")
    patronymic  = forms.CharField(max_length=48, required=False, label="Отчество")
    post = forms.ModelChoiceField(Post.objects.all(), required=True, label='Должность')
    status = forms.CharField(max_length=128, required=False, label='Статус')
    degree = forms.ModelChoiceField(AcademicDegree.objects.all(), required=False, label='Степень')
    deparment = forms.ModelChoiceField(Department.objects.all(), required=True, label='Кафедра')
    ishead = forms.BooleanField(label='Глава')

    def save(self):
        pass
        # cleaned_data = self.cleaned_data
        # result = Account.objects.raw(f"select * from create_account('{cleaned_data['first_name']}', '{cleaned_data['last_name']}', '{cleaned_data['patronymic']}')")
        # print(result[0].accountid)
        # StudentProfile.objects.raw(f"select * from create_student({result[0].id}, {cleaned_data['group']}, {cleaned_data['year']})")