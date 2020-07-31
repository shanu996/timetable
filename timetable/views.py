from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import Tables
from .forms import HomeForm
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist

@login_required
def index(request):
    try:
        t = Tables.objects.get(user=request.user)
        print(t)
        return render(request, 'tablecreationpage.html', {'exist' : True, 'timetable':t.timetable})
    except ObjectDoesNotExist:
        print("doesnotexist")
        return render(request, 'tablecreationpage.html', {'exist' : False})
def sign_up(request):
    context = {}
    form = UserCreationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            login(request,user)
            return render(request, 'tablecreationpage.html', {'exist' : False})
    context['form']=form
    return render(request,'registration/sign_up.html',context)

def post(request):
    # t = Tables.objects.update_or_create(id=1, user=request.user, timetable=request.POST.get('question'))
    


    try:
        t = Tables.objects.get(user=request.user)
        t.timetable = request.POST.get('question')
        t.save()
        print(t)
    except ObjectDoesNotExist:
        t = Tables(user= request.user, timetable=request.POST.get('question'))
        t.save()
        print("doesnotexist")

    # t = Tables.objects.get(user=request.user, id=1)
    
    # if not t:
    #     t = Tables(user= request.user, timetable="hello", id=1)
    #     t.save()
    #     print(t.timetable)
    # else:
    #     t.update(timetable="hi", user=request.user)
    #     print(t)
    # if t:
    #     print(True)
    #     t.update()
    # else:
    #     print(False)
    #     t = Tables(user= request.user, timetable=request.POST.get('question'), id=1)
    #     t.save()
    # # print()
    # Tables.objects.all().delete()
    # t = Tables.objects.filter(user=request.user, id=1)
    
    # if t:
    #     print(True)
    # else:
    #     print(False)
    return HttpResponse(200)


def viewData(request):
     t = Tables(user= request.user, timetable="hello")


def tableCreationPage(request):
    try:
        t = Tables.objects.get(user=request.user)
        print(t)
        return render(request, 'tablecreationpage.html', {'exist' : True, 'timetable':t.timetable})
    except ObjectDoesNotExist:
        print("doesnotexist")
        return render(request, 'tablecreationpage.html', {'exist' : False})
        
    # for x in t:
    #     print(x)
    # if t:
    #     print(True)
    #     return render(request, 'tablecreationpage.html', {'exist' : True, 'timetable': t.timetable})
    # else:
    #     print(False)
    