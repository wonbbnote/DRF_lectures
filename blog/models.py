from tkinter import CASCADE
from django.db import models
from user.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField("카테고리 이름", max_length=20)
    description = models.TextField("설명")

    def __str__(self):
        return self.name

class Article(models.Model):
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField("글 제목", max_length=30)
    category = models.ManyToManyField(Category, verbose_name="유저")
    contents = models.TextField("글 내용")


class Comment(models.Model):
    user = models.ForeignKey(User, verbose_name= "작성자",on_delete=models.CASCADE)
    article = models.ForeignKey(Article, verbose_name= "게시글", on_delete=models.CASCADE)
    contents = models.TextField("댓글 내용")
