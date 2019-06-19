from django.shortcuts import render,get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from .forms import todoform
from .models import todomodel
from django.urls import reverse
# Create your views here.


def index(request):
    mydict = {}
    return render(request,'index.html',mydict)
@login_required
def todo(request):
    forms = todoform()
    if request.method == 'POST':
        print("submition try")
        recived = todoform(request.POST)

        print('form recived')
        if recived.is_valid():
            print('form validate')
            username = request.user.username
            titlename = recived.cleaned_data['Title']
            discriptiondata = recived.cleaned_data['Discription']

            todo_object = todomodel.objects.create(author = username,Title = titlename,Discription = discriptiondata)
            todo_object.save()

            return HttpResponseRedirect('/homepage')
        else:
            print(recived.errors)
            print("form invalid")

    return render(request,'todos/todo.html',{'form':forms})


@login_required
def homepage(request):
    my_tasks = []
    username = request.user.username
    alltodo = todomodel.objects.all()
    for todoobject in alltodo:
        if todoobject.author == username:
            my_tasks.append(todoobject)

    dict = {"tasks" : my_tasks}
    return render(request,'todos/homepage.html',dict)


def log_in(request):
    return render(request,'user/login.html')

def sign_in(request):
    form = UserCreationForm()
    if request.method == 'POST':
        recived = UserCreationForm(request.POST)
        if recived.is_valid():
            recived.save()
            username = recived.cleaned_data['username']
            password = recived.cleaned_data['password1']

            user = authenticate(username = username,password = password)
            login(request,user)
            return HttpResponseRedirect('/homepage')

    dict = {'form' : form}
    return render(request,'user/signin.html',dict)

def log_out(request):
    logout(request)
    return HttpResponseRedirect('/login/')

@login_required
def delete(request, todoid):
    entry = get_object_or_404(todomodel, id=todoid)
    entry.delete()

    return HttpResponseRedirect('/homepage')
