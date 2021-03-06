from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.

def signup1(request):
    return render(request, 'signup.html')


def login1(request):
    return render(request, 'login.html')

def signup(request):
    if request.method == 'POST': #정보를 전달하는 방식
        if request.POST['password1'] == request.POST['password2']: #비밀번호 확인
            #유저를 만들어 줌
            user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
            #로그인하는 함수
            auth.login(request, user)
            return redirect('home') #성공하면
    return render(request,'signup.html') #실패하면

def login(request):
    if request.method == 'POST': #정보를 전달하는 방식
        username = request.POST['username']
        password = request.POST['password']
        #회원정보가 있는지 확인
        user = auth.authenticate(request, username=username, password=password)
        if user is not None: #있으면
            auth.login(request, user)
            return redirect('home')
        else: #없으면
            return render(request, 'login.html', {'error': 'username or password is incorrect'})
    else:
        return render(request,'login.html') #실패하면

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
    return render(request, 'login.html')