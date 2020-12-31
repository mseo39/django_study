from django.db import models

# Create your models here.

class Blog(models.Model):
    title=models.CharField(max_length=200) #title이라는 변수의 데이터 형식 짧은 문자열
    pub_date=models.DateTimeField('date published')
    body=models.TextField() #좀 더 긴 문자열  
    
    #python manage.py makemigrations 
    #python manage.py migrate

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100] #100글자만 보이게