from django.shortcuts import render
from rest_framework.views import APIView

class register(APIView):

    def post(self,request,format=None):
        serializer=UserRegister(data=request.data)

