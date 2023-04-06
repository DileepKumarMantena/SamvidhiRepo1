from rest_framework import generics
from rest_framework.decorators import parser_classes
from rest_framework.response import Response
from ..serializers import TeacherRegistrationSerializer
from ..models import TeachingModel


class TeacherUpdateApi(generics.GenericAPIView):
    serializer_class = TeacherRegistrationSerializer

    def put(self, request,TeacherId, *args):
        try:
            userdata = TeachingModel.objects.get(TeacherId=TeacherId)
            s = TeacherRegistrationSerializer(userdata, data=request.data)
            s.is_valid(raise_exception=True)
            s.save()

            return Response({
                'message': 'Successful',
                'Result': True,
                'HasError': False,
                'status': 200
            })
        except TeachingModel.DoesNotExist as e:
            return Response({
                'message': 'Not Updated',
                'Result': False,
                'HasError': True,
                'status': 400
            })
