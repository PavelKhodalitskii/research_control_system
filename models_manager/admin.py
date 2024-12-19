from django.contrib import admin
from .models import (
    AcademicDegree,
    Account,
    Commitette,
    Department,
    Event,
    Faculty,
    GraduateStudentProfile,
    StudentGroups,
    Post,
    RelationGraduatestudentCommitette,
    RelationTeachersCommitette,
    Research,
    ResearchParticipants,
    Speciality,
    StudentProfile,
    TeacherProfile,
)

@admin.register(AcademicDegree)
class AcademicDegreeAdmin(admin.ModelAdmin):
    list_display = [field.name for field in AcademicDegree._meta.fields]

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Account._meta.fields]

@admin.register(Commitette)
class CommitetteAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Commitette._meta.fields]

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Department._meta.fields]

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Event._meta.fields]

@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Faculty._meta.fields]

@admin.register(GraduateStudentProfile)
class GraduateStudentProfileAdmin(admin.ModelAdmin):
    list_display = [field.name for field in GraduateStudentProfile._meta.fields]

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Post._meta.fields]

@admin.register(RelationGraduatestudentCommitette)
class RelationGraduatestudentCommitetteAdmin(admin.ModelAdmin):
    list_display = [field.name for field in RelationGraduatestudentCommitette._meta.fields]

@admin.register(RelationTeachersCommitette)
class RelationTeachersCommitetteAdmin(admin.ModelAdmin):
    list_display = [field.name for field in RelationTeachersCommitette._meta.fields]

@admin.register(Research)
class ResearchAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Research._meta.fields]

@admin.register(ResearchParticipants)
class ResearchParticipantsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ResearchParticipants._meta.fields]

@admin.register(Speciality)
class SpecialityAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Speciality._meta.fields]

@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    list_display = [field.name for field in StudentProfile._meta.fields]

@admin.register(TeacherProfile)
class TeacherProfileAdmin(admin.ModelAdmin):
    list_display = [field.name for field in TeacherProfile._meta.fields]

@admin.register(StudentGroups)
class GroupsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in StudentGroups._meta.fields]
# Register your models here.

# @admin.register()