from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions

from .models import *
#from DRF.permissions import RegistedMoreThanAWeekUser
from DRF.permissions import IsAdminOrIsAuthenticatedReadOnly
from user.serializer import ArticleSerializer

from datetime import datetime

# Create your views here.

class ArticleView(APIView):
    permission_classes = [IsAdminOrIsAuthenticatedReadOnly]
    # permission_classes = [RegisteredMoreThanThreeDaysUser]
    # def get(self, request):
    #     user = request.user
    #     articles = Article.objects.filter(writer=user)
    #     titles = [article.title for article in articles]
    #     return Response({"article_list": titles})

    # permission_classes = [RegistedMoreThanAWeekUser]
    def get(self, request):
        today = datetime.now()
        articles = Article.objects.filter(
            exposure_start_date__lte = today,
            exposure_end_date__gte = today
        ).order_by('-exposure_start_date')
        print(articles)

        return Response(ArticleSerializer(articles, many=True).data)
        #return Response({'message':"b"})


    def post(self, request):
        user = request.user
        title = request.data.get("title", "")
        contents = request.data.get("contents", "")
        categorys = request.data.pop("category", [])


        if len(title)<=5:
            return Response({"error": "제목은 5자 이상!"})
        if len(contents) <= 20:
            return Response({"error": "내용은 20자 이상!"})
        if not categorys:
            return Response({"error": "카테고리 지정!"})
        
        article = Article(writer=user, title=title, contents=contents)
        article.save()
        article.category.add(*categorys)

        return Response({"message":"글 작성!"})