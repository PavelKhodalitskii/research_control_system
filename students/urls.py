from django.urls import path
from .views import StudentTableView, CreateStudentView, StudentDetailView, delete_student, delete_several_students

urlpatterns = [
    path('table/', StudentTableView.as_view(), name='students_table'),
    path('create/', CreateStudentView.as_view(), name='create_student'),
    path('info/<int:account_id>/', StudentDetailView.as_view(), name='student_details'),
    path('delete_several/', delete_several_students, name='delete_several_students'),
    path('delete/<int:account_id>/', delete_student, name='delete_student')
]