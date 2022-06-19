from xml.etree.ElementTree import Comment
from rest_framework import serializers

from user.models import User as UserModel
from user.models import UserProfile as UserProfileModel
from blog.models import Article as ArticleModel

class ArticleSerializer(serializers.ModelSerializer):
    user_article = serializers.SerializerMethodField()
    def get_user_article(self, obj):
        return "TEST!!"

    class Meta:
        model = ArticleModel
        fields = ["article", "comment", "user_article"]

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"

class UserProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UserProfileModel
        fields = ["introduction","birthday", "age"]

class UserSerializer(serializers.ModelSerializer):
    userprofile = UserProfileSerializer()
    articles = ArticleSerializer(many=True, source="article_set")
    comments = CommentSerializer(many=True, source="comment_set")
    class Meta:
        model = UserModel
        fields = ["username", "email", "fullname", "join_date", "userprofile", "articles", "comments"]