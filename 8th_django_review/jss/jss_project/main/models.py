from django.db import models

# Create your models here.

class Jasoseol(models.Model): #첫글자는 대문자 models의 Model을 상속받음
    title = models.CharField(max_length=50)
    content = models.TextField()
    updated_at = models.DateTimeField(auto_now=True) #날짜와 시간을 받을 수 있음 auto_now 날짜와 시간을 자동으로 저장 해줌