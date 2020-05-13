
from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import UserRegisterForm,LoginForm
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout,get_user_model
from django.contrib.auth.decorators import login_required



def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'  Account created   for {username} you have to login')
            return redirect('login')
    
    else:
        form = UserRegisterForm()
    return render(request, 'student/register.html', {'form': form})


def login_view(request):
    form = LoginForm(request.POST or None)
    context = {
        'form': form
    }
    print(request.user.is_authenticated)
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('/home/')
        else:
            print("error.......")
    return render(request, "student/login.html", context=context)

def logout_view(request):
    logout(request)
    return redirect('/login/')
           
@login_required(login_url="login")
def home(request):
    return render(request, 'student/home.html')

@login_required(login_url="profile")
def profile(request):
    return render(request, 'student/profile.html')
@login_required(login_url="about")
def about(request):
    return HttpResponse('<h2>hello  </h2>')
