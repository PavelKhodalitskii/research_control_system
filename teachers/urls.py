from django.urls import path
from .views import TeacherTableView, CreateTeacherView, TeacherDetailView, delete_several_teachers, delete_teacher

urlpatterns = [
    path('table/', TeacherTableView.as_view(), name='teachers_table'),
    path('create/', CreateTeacherView.as_view(), name='create_teacher'),
    path('info/<int:account_id>/', TeacherDetailView.as_view(), name='teacher_details'),
    path('delete_several/', delete_several_teachers, name='delete_several_teachers'),
    path('delete/<int:account_id>/', delete_teacher, name='delete_teacher')
]