from django.shortcuts import render

# Create your views here.

def home(request):
    #queryset을 templates로 보내기
    deginers = Deginer.objects.all()
    return render(request,'home.html')
    #전해줄 값을 딕셔너리로 작성함
def introduce(request):
    return render(request,'introduce.html')