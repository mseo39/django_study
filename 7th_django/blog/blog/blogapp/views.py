from django.shortcuts import render ,get_object_or_404
from .models import Blog

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