from django.shortcuts import render
from .models import HeroInfo


# Create your views here.
def index(request):
    #hero = HeroInfo.objects.get(id=15)
    #context = {'hero': hero}
    #context = {}
    list = HeroInfo.objects.all()
    context = {'list':list}
    return render(request, 'booktest/index.html', context)