from django.db import models

# Create your models here.

class Designer(models.Model): #모델명의 첫글자는 대문자로
    image = models.ImageField(upload_to= 'images/') #이미지를 다루기 위해 pillow설치
    name = models.CharField(max_length = 50) #최대로 넣을 수 있는 글자 수
    address = models.CharField(max_length = 255)
    description = models.TextField()
    #변수명=데이터형식

    def __str__(self): #제목에 오브젝트가 아니라 이름이 나오도록
        return self.name
 
#python manage.py makemigrations (+앱이름)_DB가 알아 듣도록 번역 
#python manage.py migrate (+앱이름)_번역한 내용을 DB에 전송
#(+앱이름을 작성하면 특정 앱만 db가 알아들음)