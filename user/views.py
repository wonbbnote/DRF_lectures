from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions

from django.contrib.auth import login, logout, authenticate

from user.serializer import UserSerializer

class UserApiView(APIView):
    def get(self, request):
        return Response(UserSerializer(request.user).data)
    # 로그인
    def post(self, request):
        username = request.data.get('username', '')
        password = request.data.get('password', '')
        user = authenticate(request, username=username, password=password)

        if not user:
            return Response({'error':'존재하지 않는 계정이거나 패스워드가 일치하지 않습니다.'})
        login(request, user)

        serialized_user_data = UserSerializer(user).data
        return Response(serialized_user_data)

    #로그아웃
    def delete(self, request):
        logout(request)
        return Response({'message':'logout success!!'})
