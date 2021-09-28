from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import StudentSerializer
from .models import Student

# Create your views here.
class StudentView(APIView):
    def get(self, request, *args, **kwargs):
        query_set = Student.objects.all()
        serializer = StudentSerializer(query_set, many=True)
        return Response(serializer.data)


class SecondView(APIView):
    def get(self, request, *args, **kwargs):
        query_set = Student.objects.all()
        serializer = StudentSerializer(query_set, many=True)
        return Response(serializer.data)