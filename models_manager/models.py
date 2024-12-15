# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.urls import reverse

class AcademicDegree(models.Model):
    '''
    Научная степень
    '''
    academicdegreename = models.CharField(max_length=128, blank=True, null=True, verbose_name='Имя научной степени')

    def __str__(self):
        return self.academicdegreename if self.academicdegreename else repr(self)

    class Meta:
        managed = False
        db_table = 'academicdegree'
        verbose_name = 'Научная степень'
        verbose_name_plural = 'Научные степени'

class Account(models.Model):
    '''
    Аккаунт пользователя
    '''
    firstname = models.CharField(max_length=128, verbose_name="Имя")
    lastname = models.CharField(max_length=128, verbose_name="Фамилия")
    patronymic = models.CharField(max_length=128, blank=True, null=True, verbose_name="Отчество")

    def __str__(self):
        return str(self.firstname) + " " + str(self.lastname) + " " + str(self.patronymic)

    class Meta:
        managed = False
        db_table = 'account'
        verbose_name = 'Аккаунт'
        verbose_name_plural = 'Аккаунты'        

# class AuthUser(models.Model):
#     password = models.CharField(max_length=128)
#     last_login = models.DateTimeField(blank=True, null=True)
#     is_superuser = models.BooleanField()
#     username = models.CharField(unique=True, max_length=150)
#     first_name = models.CharField(max_length=150)
#     last_name = models.CharField(max_length=150)
#     email = models.CharField(max_length=254)
#     is_staff = models.BooleanField()
#     is_active = models.BooleanField()
#     date_joined = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'auth_user'

class Commitette(models.Model):
    '''
    Комитет по НИР
    '''
    chairman = models.ForeignKey('Teacherprofile', models.DO_NOTHING, db_column='chairman', blank=True, null=True, verbose_name="Председатель")

    class Meta:
        managed = False
        db_table = 'commitette'
        verbose_name = 'Комитет'
        verbose_name_plural = 'Комитеты'

class Department(models.Model):
    '''
    Кафедра
    '''
    name = models.CharField(max_length=512, verbose_name="Название")
    faculty = models.ForeignKey('Faculty', models.DO_NOTHING, db_column='faculty', blank=True, null=True, verbose_name="Факультет")

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'department'
        verbose_name = 'Кафедра'
        verbose_name_plural = 'Кафедры'

class Event(models.Model):
    '''
    Событие
    '''
    name = models.CharField(max_length=512, verbose_name="Название")
    type = models.CharField(max_length=256, blank=True, null=True, verbose_name="Тип")
    addresscity = models.CharField(max_length=128, blank=True, null=True, verbose_name="Город")
    addressstreet = models.CharField(max_length=128, blank=True, null=True, verbose_name="Улица")
    addressnumber = models.CharField(max_length=128, blank=True, null=True, verbose_name="Здание(Номер)")
    date = models.DateField(blank=True, null=True, verbose_name="Дата")
    faculty = models.ForeignKey('Faculty', models.DO_NOTHING, db_column='faculty', blank=True, null=True, verbose_name="Факультет")

    def __str__(self):
        return self.name + " " + str(self.date)

    def get_absolute_url(self):
        return reverse('event_details', kwargs={'event_id': self.id})

    class Meta:
        managed = False
        db_table = 'event'
        verbose_name = 'Событие'
        verbose_name_plural = 'События'

class Faculty(models.Model):
    '''
    Факультет
    '''
    name = models.CharField(max_length=256, verbose_name="Название")

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'faculty'
        verbose_name = 'Факультет'
        verbose_name_plural = 'Факультеты'

class GraduateStudentProfile(models.Model):
    '''
    Профиль аспиранта
    '''
    year = models.IntegerField(verbose_name="Курс")
    studgroup = models.ForeignKey('StudentGroups', models.DO_NOTHING, db_column='studgroup', blank=True, null=True, verbose_name="Группа")
    account = models.ForeignKey(Account, models.DO_NOTHING, db_column='account', blank=True, null=True, verbose_name="Аккаунт")

    def __str__(self):
        return " ".join([self.account.firstname, self.account.lastname])

    class Meta:
        managed = False
        db_table = 'graduatestudentprofile'
        verbose_name = 'Профиль аспиранта'
        verbose_name_plural = 'Профили аспирантов'

class StudentGroups(models.Model):
    '''
    Группа
    '''
    name = models.CharField(max_length=64, verbose_name="Название")
    specialty = models.ForeignKey('Speciality', models.DO_NOTHING, db_column='specialty', blank=True, null=True, verbose_name="Специальность")

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'groups'
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'

class Post(models.Model):
    '''
    Должность
    '''
    postname = models.CharField(max_length=128, blank=True, null=True, verbose_name="Название должности")
    
    def __str__(self):
        return self.postname

    class Meta:
        managed = False
        db_table = 'post'
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'

class RelationGraduatestudentCommitette(models.Model):
    '''
    Отношение аспирант-комитет
    '''
    graduatestudentprofile = models.ForeignKey(GraduateStudentProfile, models.DO_NOTHING, db_column='graduatestudentprofile', blank=True, null=True, verbose_name="Аспирант")
    commitette = models.ForeignKey(Commitette, models.DO_NOTHING, db_column='commitette', blank=True, null=True, verbose_name="Комитет")

    class Meta:
        managed = False
        db_table = 'relationgraduatestudentcommitette'
        verbose_name = 'Отношение аспирант-комитет'
        verbose_name_plural = 'Отношение аспирант-комитет'

class RelationTeachersCommitette(models.Model):
    '''
    Отношение преподаватель-комитет
    '''
    teacherprofile = models.ForeignKey('Teacherprofile', models.DO_NOTHING, db_column='teacherprofile', blank=True, null=True, verbose_name="Преподаватель")
    commitette = models.ForeignKey(Commitette, models.DO_NOTHING, db_column='commitette', blank=True, null=True, verbose_name="Комитет")

    class Meta:
        managed = False
        db_table = 'relationteacherscommitette'
        verbose_name = 'Отношение преподаватель-комитет'
        verbose_name_plural = 'Отношение преподаватель-комитет'

class Research(models.Model):
    '''
    НИР
    '''
    commitette = models.ForeignKey(Commitette, models.DO_NOTHING, db_column='commitette', blank=True, null=True, verbose_name="Комитет")
    event = models.ForeignKey(Event, models.DO_NOTHING, db_column='event', blank=True, null=True, verbose_name="Событие")

    class Meta:
        managed = False
        db_table = 'research'
        verbose_name = 'НИР'
        verbose_name_plural = 'НИР'

class ResearchParticipants(models.Model):
    '''
    Участники исследования
    '''
    research = models.ForeignKey(Research, models.DO_NOTHING, db_column='research', blank=True, null=True, verbose_name="Исследование")
    account = models.ForeignKey(Account, models.DO_NOTHING, db_column='account', blank=True, null=True, verbose_name="Аккаунт")

    class Meta:
        managed = False
        db_table = 'researchparticipants'
        verbose_name = 'Участники исследования'
        verbose_name_plural = 'Участники исследования'

class Speciality(models.Model):
    '''
    Спциальность
    '''
    name = models.CharField(max_length=256, verbose_name="Название")
    department = models.ForeignKey(Department, models.DO_NOTHING, db_column='department', blank=True, null=True, verbose_name="Кафедра")

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'speciality'
        verbose_name = 'Спциальность'
        verbose_name_plural = 'Спциальности'

class StudentProfile(models.Model):
    '''
    Профиль студента
    '''
    year = models.IntegerField()
    studgroup = models.ForeignKey(StudentGroups, models.DO_NOTHING, db_column='studgroup', blank=True, null=True, verbose_name="Группа")
    account = models.ForeignKey(Account, models.DO_NOTHING, db_column='account', blank=True, null=True, verbose_name="Аккаунт")

    def __str__(self):
        return " ".join([self.account.firstname, self.account.lastname])

    class Meta:
        managed = False
        db_table = 'studentprofile'
        verbose_name = 'Профиль студента'
        verbose_name_plural = 'Профили студентов'

class TeacherProfile(models.Model):
    '''
    Профиль преподавателя
    '''
    post = models.ForeignKey(Post, models.DO_NOTHING, db_column='post', blank=True, null=True, verbose_name="Должность")
    status = models.CharField(max_length=256, blank=True, null=True, verbose_name="Статус")
    degree = models.ForeignKey(AcademicDegree, models.DO_NOTHING, db_column='degree', blank=True, null=True, verbose_name="Степень")
    account = models.ForeignKey(Account, models.DO_NOTHING, db_column='account', blank=True, null=True, verbose_name="Аккаунт")
    department = models.ForeignKey(Department, models.DO_NOTHING, db_column='department', blank=True, null=True, verbose_name="Кафедра")
    ishead = models.BooleanField(blank=True, null=True, verbose_name="Глава кафедры")

    def __str__(self):
        return " ".join([self.account.firstname, self.account.lastname])

    class Meta:
        managed = False
        db_table = 'teacherprofile'
        verbose_name = 'Профиль преподавателя'
        verbose_name_plural = 'Профили преподавателей'
