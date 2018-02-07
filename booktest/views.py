from django.shortcuts import render
from django.http import HttpResponse
from .models import HeroInfo


# Create your views here.
def index(request):
    #hero = HeroInfo.objects.get(id=15)
    #context = {'hero': hero}
    #context = {}
    list = HeroInfo.objects.all()
    context = {'list': list}
    return render(request, 'booktest/index.html', context)

def show(request,id):
    context = {'id': id}
    return render(request, 'booktest/show.html', context)

#用于练习模板的继承
def index2(request):
    return render(request, 'booktest/index2.html')

def user1(request):
    context = {'uname':'chunjue'}
    # user1得到的参数 可以显示到它的父级里 在base里{{ uname }}
    return render(request, 'booktest/user1.html', context)

def user2(request):
    return render(request, 'booktest/user2.html')

#html转义
def htmlTest(request):
    context = {'t1':'<h1>123</h1>'}
    return render(request, 'booktest/htmlTest.html', context)

#CSRF 跨站请求伪造
def csrf1(request):
    return render(request, 'booktest/csrf1.html')

def csrf2(request):
    uname = request.POST['uname']
    return HttpResponse(uname)