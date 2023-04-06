from rest_framework import generics
from rest_framework.decorators import parser_classes
from rest_framework.response import Response
from ..serializers import TeacherRegistrationSerializer
from ..models import TeachingModel
from rest_framework.parsers import MultiPartParser


@parser_classes((MultiPartParser,))
class TeacherDeleteApi(generics.GenericAPIView):
    serializer_class = TeacherRegistrationSerializer

    def delete(self, request, TeacherId):
        try:
            d = TeachingModel.objects.get(TeacherId=TeacherId)
            d.delete()
            return Response({
                'message': 'Successful',
                'Result': True,
                'HasError': False,
                'status': 200
            })
        except TeachingModel.DoesNotExist as e:
            return Response({
                'message': 'Book Not Found',
                'Result': False,
                'HasError': True,
                'status': 400
            })
