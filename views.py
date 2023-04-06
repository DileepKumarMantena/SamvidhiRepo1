from django.shortcuts import render

# Create your views here.
from .Teacher_Crud.teacher_registration_api import TeacherRegistrationApi
from .Teacher_Crud.teacher_get_api import TeachersGetAllApi
from .Teacher_Crud.teachers_get_api_by_id import TeachersGetByIdApi
from .Teacher_Crud.teacher_update_api import TeacherUpdateApi
from .Teacher_Crud.teachers_delete_api import TeacherDeleteApi

TeacherRegistrationApi()
TeachersGetAllApi()
TeachersGetByIdApi()
TeacherUpdateApi()
TeacherDeleteApi()