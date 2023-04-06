from django.apps import apps
from rest_framework import serializers
from .models import *


class TeacherRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeachingModel
        fields = ['CourseInstructor', 'Course', 'ClassSize', 'TeacherId', 'NativeEnglishSpeaker', 'Semester',
                  'PerformanceScore']
        # fields = "__all__"
        extra_kwargs = {'Password': {'write_only': True}, }

    def create(self, validated_data):
        user = TeachingModel.objects.create(CourseInstructor=validated_data['CourseInstructor'],
                                            Course=validated_data['Course'],
                                            ClassSize=validated_data['ClassSize'],
                                            TeacherId=validated_data['TeacherId'],
                                            NativeEnglishSpeaker=validated_data['NativeEnglishSpeaker'],
                                            Semester=validated_data['Semester'],
                                            PerformanceScore=validated_data['PerformanceScore'])

        user.save()
        return user
