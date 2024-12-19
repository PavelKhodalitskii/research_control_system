from django.urls import path, include
from .views import (StudentTableView, 
                    CreateStudentView, 
                    StudentDetailView,
                    GraduatesTableView,
                    GraduatesCreateView,
                    GraduateDetailView, 
                    delete_student,
                    delete_several_students)

from .service import StudentController, GraduateStudentController

urlpatterns = [
    path('table/', StudentTableView.as_view(), name='students_table'),
    path('create/', CreateStudentView.as_view(), name='create_student'),
    path('info/<int:account_id>/', StudentDetailView.as_view(), name='student_details'),
    path('delete_several/', StudentController.delete_several_students, name='delete_several_students'),
    path('delete/<int:account_id>/', StudentController.delete_student, name='delete_student'),
    path('graduate/', include([
        path('table/', GraduatesTableView.as_view(), name='graduates_table'),
        path('create/', GraduatesCreateView.as_view(), name='create_graduate'),
        path('info/<int:account_id>/', GraduateDetailView.as_view(), name='graduate_details'),
        path('delete_several/', GraduateStudentController.delete_several_students, name='delete_several_graduates'),
        path('delete/<int:account_id>/', GraduateStudentController.delete_student, name='delete_graduate'),
    ]))
]