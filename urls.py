from django.urls import path
from .views import *

urlpatterns = [
    path('TeacherRegistrationApi/', TeacherRegistrationApi.as_view()),
    path('TeachersGetAllApi/', TeachersGetAllApi.as_view()),
    path('TeachersGetByIdApi/<int:TeacherId>/', TeachersGetByIdApi.as_view()),
    path('TeacherUpdateApi/<int:TeacherId>/', TeacherUpdateApi.as_view()),
    path('TeacherDeleteApi/<int:TeacherId>/', TeacherDeleteApi.as_view()),

]
