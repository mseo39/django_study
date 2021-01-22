from django.shortcuts import render, redirect, get_object_or_404
from main.models  import Designer #모델의 존재 알려주기
# Create your views here.

def home(request):
    #queryset을 templates로 보내기
    designer = Designer.objects.all()
    return render(request,'home.html', {'designer':designer})
    #전해줄 값을 딕셔너리로 작성함
def introduce(request):
    return render(request,'introduce.html')

def detail(request, designer_id):
    designer = get_object_or_404(Designer, pk=designer_id)
    return render(request, 'detail.html', {'designer' : designer})

def new(request):
    return render(request, 'new.html')

def create(request):
    if request.method == 'POST':
        post = Designer()
        if 'image' in request.FILES:
            post.image = request.FILES['image']
            post.name = request.POST['name']
            post.address = request.POST['address']
            post.description = request.POST['description']
            post.save()
        return redirect('detail', post.id)

def update(request, designer_id):
    post = get_object_or_404(Designer, pk = designer_id)
    if request.method == 'POST':
        if 'image' in request.FILES:
            post.image = request.FILES['image']
            post.name = request.POST['name']
            post.address = request.POST['address']
            post.description = request.POST['description']
            post.save()
        return redirect('detail', post.id)
    else:
        return render(request, 'update.html', {'designer' : post})

def delete(request, designer_id):
    post = get_object_or_404(Designer, pk=designer_id)
    post.delete()
    return redirect('home')