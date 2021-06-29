from django.contrib.auth import authenticate, login as loginUser, logout #login user and logout user
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import  NOTES 
from .forms import NOTESFORM
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def home(request):
    form =NOTESFORM()
    Notes =NOTES.objects.all()
    context={
        'form':form,
        'NOTES':Notes
    }
    return render(request, 'index.html', context)

def login(request):
    if request.method == 'GET':
        form = AuthenticationForm()
        context = {
            'form': form
        }
        return render(request, 'login.html', context)
    else:
        form = AuthenticationForm(data=request.POST)
        print(form.is_valid)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                loginUser(request, user)
                return redirect('home')

        else:
            context = {
                "form": form

            }
            return render(request, 'login.html', context)

def signup(request):
    if request.method == 'GET':
        form = UserCreationForm()
        context = {
            'form': form
        }
        return render(request, 'signup.html', context=context)
    else:
        print(request.POST)
        form = UserCreationForm(request.POST)

        context = {
            'form': form
        }
        if form.is_valid():
            user = form.save()
            print(user)
            if user is not None:
                return redirect('login')
        else:
            return render(request, 'signup.html', context=context)

@login_required(login_url='login')
def add_tonote(request):
    if request.user.is_authenticated:#if user is logged in 
        user = request.user #getting logged in user
        print(user)#to see user
        if request.method == "POST":
            form=NOTESFORM(request.POST,request.FILES)
            context = {
            'form':form
             }
        if form.is_valid():
             print(form.cleaned_data)
             todo= form.save(commit=False)
             todo.user=user
             todo.save()
             print(todo)#print saved to do in console
             return redirect("home")
        else:
            return render(request, 'index.html', context)  



def delete_notes(rqquest,id):
    NOTES.objects.get(pk=id).delete()
    return redirect('home')



def signout(request):
    logout(request)
    return  redirect('login')
