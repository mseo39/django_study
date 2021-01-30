from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Jasoseol(models.Model): #첫글자는 대문자 models의 Model을 상속받음
    title = models.CharField(max_length=50)
    content = models.TextField()
    updated_at = models.DateTimeField(auto_now=True) #날짜와 시간을 받을 수 있음 auto_now 날짜와 시간을 자동으로 저장 해줌
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True) #빈값도 허용

class Comment(models.Model):
    content = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    jasoseol = models.ForeignKey(Jasoseol, on_delete=models.CASCADE)