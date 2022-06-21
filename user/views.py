from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions

from django.contrib.auth import login, logout, authenticate

from .serializer import UserSerializer

from DRF.permissions import IsAdminOrIsAuthenticatedReadOnly

class UserView(APIView): # CBV 방식
    permission_classes = [IsAdminOrIsAuthenticatedReadOnly] 
    
    def get(self, request):
		# 사용자 정보조회
        return Response(UserSerializer(request.user).data)
        # return Response({'message': 'get method!!'})
        
    def post(self, request):
		# 회원가입
        return Response({'message': 'post method!!'})

    def put(self, request):
		# 회원 정보 수정
        return Response({'message': 'put method!!'})

    def delete(self, request):
		# 회원 탈퇴
        return Response({'message': 'delete method!!'})






class UserApiView(APIView):
        
    # 로그인
    def post(self, request):
        username = request.data.get('username', '')
        password = request.data.get('password', '')
        user = authenticate(request, username=username, password=password)

        if not user:
            return Response({'error':'존재하지 않는 계정이거나 패스워드가 일치하지 않습니다.'})
        login(request, user)
        return Response({'message':'login success!!'})

    #로그아웃
    def delete(self, request):
        logout(request)
        return Response({'message':'logout success!!'})
