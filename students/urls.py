from django.urls import path
from .views import StudentTableView, CreateStudentView, StudentDetailView, delete_student, delete_several_students

urlpatterns = [
    path('table/', StudentTableView.as_view(), name='students_table'),
    path('create/', CreateStudentView.as_view(), name='create_student'),
    path('info/<int:student_id>/', StudentDetailView.as_view(), name='student_details'),
    path('delete_several/', delete_several_students, name='delete_several_students'),
    path('delete/<int:student_id>/', delete_student, name='delete_student')
]