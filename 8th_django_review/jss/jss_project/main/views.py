from django.shortcuts import render, redirect, get_object_or_404
from .forms import JssForm, CommentForm
from .models import Jasoseol, Comment
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
# Create your views here.

def index(request):
    all_jss= Jasoseol.objects.all()
    return render(request, 'index.html', {'all_jss':all_jss})

def my_index(request):
    my_jss= Jasoseol.objects.filter(author=request.user)
    return render(request, 'index.html', {'all_jss':my_jss})

@login_required(login_url='/login/') #방법1
def create(request):
    # 방법2 if not request.user.is_authenticated: 로그인이 안되어 있으면 login페이지로 이동
        # return redirect('login')

    if request.method == "POST":
        filled_form = JssForm(request.POST)
        if filled_form.is_valid():
            temp_form= filled_form.save(commit=False)
            temp_form.author = request.user
            filled_form.save()
            return redirect('index')

    jss_form=JssForm()
    return render(request, 'create.html', {'jss_form':jss_form})

@login_required(login_url='/login/')
def detail(request, jss_id):

    # try: #페이지가 있다면
    #     my_jss = Jasoseol.object.get(pk=jss_id) #.get으로 하나의 object만 보내줌

    # except:#페이지가 없다면
    #     raise Http404

    my_jss=get_object_or_404(Jasoseol, pk=jss_id)
    comment_form=CommentForm()
    return render(request, 'detail.html', {'my_jss':my_jss, 'comment_form':comment_form})


def delete(request, jss_id):
    my_jss = Jasoseol.objects.get(pk=jss_id)
    if request.user == my_jss.author:
         my_jss.delete() 
         return redirect('index')
    raise PermissionDenied
        

def update(request, jss_id):
    my_jss = Jasoseol.objects.get(pk=jss_id)
    jss_form = JssForm(instance=my_jss)
    if request.method == "POST":
        updated_form= JssForm(request.POST, instance=my_jss) #instance를 작성해줘야 수정하고 싶은 오브젝트에 수정할 수 있음
        if updated_form.is_valid():
            updated_form.save()
            return redirect('index')
    return render(request,'create.html',{'jss_form':jss_form})

def create_comment(request,jss_id):
    comment_form= CommentForm(request.POST)
    if comment_form.is_valid():
        temp_form = comment_form.save(commit=False)
        temp_form.author = request.user
        temp_form.jasoseol = Jasoseol.objects.get(pk=jss_id)
        temp_form.save()

        return redirect('detail', jss_id)

def delete_comment(request, jss_id, comment_id):
    my_comment = Comment.objects.get(pk=comment_id)
    if request.user == my_comment.author:
        my_comment.delete()
        return redirect('detail', jss_id)

    else:
        raise PermissionDenied