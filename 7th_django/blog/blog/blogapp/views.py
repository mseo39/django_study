from django.shortcuts import render ,get_object_or_404, redirect
from .models import Blog
from django.utils import timezone

# Create your views here.

def home(request):
    blogs=Blog.objects #객체 목록(쿼리셋)을 전달 받
    #쿼리셋을 기능을 처리하고 정렬하는 등의 기능을 메소드라고 함
    return render(request, 'home.html',{'blogs':blogs})

    #쿼리셋과 메소드의 형식
    #모델.쿼리셋(objects).메소드
    #.all  .count .first .last 등등

def detail(request, blog_id):
    blog_detail=get_object_or_404(Blog, pk= blog_id)
    return render(request, 'detail.html', {'blog':blog_detail})

def new(request): #new.html을 띄어주는 함수
    return render(request, 'new.html')

def create(request): #입력받은 내용을 데이터베이스에 넣어주는 함수
    blog=Blog()
    blog.title=request.GET['title']
    blog.body=request.GET['body']
    blog.pub_date=timezone.datetime.now()
    blog.save() #쿼리셋 메소드 중 하나, 데이터베이스에 저장하라
    return redirect('/blog/'+str(blog.id)) #blog.id는 int형이므로 형변환을 줌

#render_데이터를 담아서 사용하고 싶을 때 redirect_단순 페이지를 띄우고 싶을 때
