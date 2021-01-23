from django.shortcuts import render, redirect, get_object_or_404
from .forms import JssForm
from .models import Jasoseol
# Create your views here.

def index(request):
    all_jss= Jasoseol.objects.all()
    return render(request, 'index.html', {'all_jss':all_jss})

def create(request):

    if request.method == "POST":
        filled_form = JssForm(request.POST)
        if filled_form.is_valid():
            filled_form.save()
            return redirect('index')

    jss_form=JssForm()
    return render(request, 'create.html', {'jss_form':jss_form})

def detail(request, jss_id):

    # try: #페이지가 있다면
    #     my_jss = Jasoseol.object.get(pk=jss_id) #.get으로 하나의 object만 보내줌

    # except:#페이지가 없다면
    #     raise Http404

    my_jss=get_object_or_404(Jasoseol, pk=jss_id)
    return render(request, 'detail.html', {'my_jss':my_jss})

def delete(request, jss_id):
    my_jss = Jasoseol.objects.get(pk=jss_id)
    my_jss.delete()
    return redirect('index')
        

def update(request, jss_id):
    my_jss = Jasoseol.objects.get(pk=jss_id)
    jss_form = JssForm(instance=my_jss)
    if request.method == "POST":
        updated_form= JssForm(request.POST, instance=my_jss) #instance를 작성해줘야 수정하고 싶은 오브젝트에 수정할 수 있음
        if updated_form.is_valid():
            updated_form.save()
            return redirect('index')
    return render(request,'create.html',{'jss_form':jss_form})