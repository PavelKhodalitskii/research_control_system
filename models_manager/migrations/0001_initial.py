# Generated by Django 5.0.6 on 2024-12-14 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AcademicDegree',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('academicdegreename', models.CharField(blank=True, max_length=128, null=True, verbose_name='Имя научной степени')),
            ],
            options={
                'verbose_name': 'Научная степень',
                'verbose_name_plural': 'Научные степени',
                'db_table': 'academicdegree',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=128, verbose_name='Имя')),
                ('lastname', models.CharField(max_length=128, verbose_name='Фамилия')),
                ('patronymic', models.CharField(blank=True, max_length=128, null=True, verbose_name='Отчество')),
            ],
            options={
                'verbose_name': 'Аккаунт',
                'verbose_name_plural': 'Аккаунты',
                'db_table': 'account',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.BooleanField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.BooleanField()),
                ('is_active', models.BooleanField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Commitette',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Комитет',
                'verbose_name_plural': 'Комитеты',
                'db_table': 'commitette',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Кафедра',
                'verbose_name_plural': 'Кафедры',
                'db_table': 'department',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512, verbose_name='Название')),
                ('type', models.CharField(blank=True, max_length=256, null=True, verbose_name='Тип')),
                ('addresscity', models.CharField(blank=True, max_length=128, null=True, verbose_name='Город')),
                ('addressstreet', models.CharField(blank=True, max_length=128, null=True, verbose_name='Улица')),
                ('addressnumber', models.CharField(blank=True, max_length=128, null=True, verbose_name='Здание(Номер)')),
                ('date', models.DateField(blank=True, null=True, verbose_name='Дата')),
            ],
            options={
                'verbose_name': 'Событие',
                'verbose_name_plural': 'События',
                'db_table': 'event',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Факультет',
                'verbose_name_plural': 'Факультеты',
                'db_table': 'faculty',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='GraduateStudentProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(verbose_name='Курс')),
            ],
            options={
                'verbose_name': 'Профиль аспиранта',
                'verbose_name_plural': 'Профили аспирантов',
                'db_table': 'graduatestudentprofile',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Groups',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Группа',
                'verbose_name_plural': 'Группы',
                'db_table': 'groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postname', models.CharField(blank=True, max_length=128, null=True, verbose_name='Название должности')),
            ],
            options={
                'verbose_name': 'Должность',
                'verbose_name_plural': 'Должности',
                'db_table': 'post',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='RelationGraduatestudentCommitette',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Отношение аспирант-комитет',
                'verbose_name_plural': 'Отношение аспирант-комитет',
                'db_table': 'relationgraduatestudentcommitette',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='RelationTeachersCommitette',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Отношение преподаватель-комитет',
                'verbose_name_plural': 'Отношение преподаватель-комитет',
                'db_table': 'relationteacherscommitette',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Research',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'НИР',
                'verbose_name_plural': 'НИР',
                'db_table': 'research',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ResearchParticipants',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Участники исследования',
                'verbose_name_plural': 'Участники исследования',
                'db_table': 'researchparticipants',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Speciality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Спциальность',
                'verbose_name_plural': 'Спциальности',
                'db_table': 'speciality',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='StudentProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Профиль студента',
                'verbose_name_plural': 'Профили студентов',
                'db_table': 'studentprofile',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TeacherProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(blank=True, max_length=256, null=True, verbose_name='Статус')),
                ('ishead', models.BooleanField(blank=True, null=True, verbose_name='Глава кафедры')),
            ],
            options={
                'verbose_name': 'Профиль преподавателя',
                'verbose_name_plural': 'Профили преподавателей',
                'db_table': 'teacherprofile',
                'managed': False,
            },
        ),
    ]