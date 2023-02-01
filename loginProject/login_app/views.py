from django.shortcuts import render
from login_app import models, forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def index(request):
    data={
        'title':'Home Page'
    }
    if request.user.is_authenticated:
        current_user = request.user
        user_id = current_user.id
        user_basic_info = User.objects.get(pk=user_id)
        user_more_info = models.UserInfo.objects.get(user__pk=user_id)
        data.update({
            'user_basic_info':user_basic_info,
            'user_more_info':user_more_info
        })
    return render(request, 'index.html', data)

def register(request):
    data={
        
    }
    registered = False
    if request.method== "POST":
        user_form = forms.UserForm(data=request.POST)
        user_info_form = forms.UserInfoForm(data=request.POST)
        if user_form.is_valid() and user_info_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            user_info = user_info_form.save(commit=False)
            user_info.user = user
            if 'profile_pic' in request.FILES:
                user_info.profile_pic = request.FILES['profile_pic']
            user_info.save()
            registered = True
    else:
        user_form = forms.UserForm()
        user_info_form=forms.UserInfoForm()  
    
    data.update({
        'title':'Register',
        'user_form':user_form,
        'user_info_form':user_info_form,
        'registered':registered
    })    
    return render(request, 'register.html', data)

def login_page(request):
    data={
        'title':"Login Page",
    }
    return render(request, 'login.html', data)

def login_user(request):
    data={
        'title':'Login Page'
    }
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('Login_App:index'))
            else:
                return HttpResponse('User is not Active!')
        else:
            return HttpResponse('Login Information Wrong!!')
    else:
        return render(request, 'login.html', data)

def user_logout(request):
    data={
        
    }
    logout(request)
    return render(request, 'login.html', data)