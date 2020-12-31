from django.db import models

# Create your models here.

class Portfolio(models.Model):
    title=models.CharField(max_length=255) #title이라는 변수의 데이터 형식 짧은 문자열
    image=models.ImageField(upload_to='images/')
    description=models.CharField(max_length=500) 
    
    #pip install pillow

    #python manage.py makemigrations 
    #python manage.py migrate

    def __str__(self):
        return self.title

    def summary(self):
        return self.description[:100] #100글자만 보이게