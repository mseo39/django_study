from django.shortcuts import render, redirect, get_object_or_404
from myapp.models  import Deginer #모델의 존재 알려주기
# Create your views here.

def home(request):
    #queryset을 templates로 보내기
    deginers = Deginer.objects.all()
    return render(request,'home.html', {'deginers':deginers})
    #전해줄 값을 딕셔너리로 작성함
def introduce(request):
    return render(request,'introduce.html')

def detail(request, designer_id):
    designer = get_object_or_404(Designer, pk=designer_id)
    return render(request, 'detail.html', {'designer' : designer})