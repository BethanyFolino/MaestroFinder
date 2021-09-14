from django.shortcuts import render, HttpResponseRedirect, reverse
from maestrofinder_app.models import Musician, Request
from maestrofinder_app.forms import SignupForm, RequestForm, LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django import forms

# Create your views here.
def index_view(request):
    return render(request, 'index.html')

def user_detail(request, id):
    musician = Musician.objects.get(id=id)
    requests = Request.objects.filter(musician=musician)
    return render(request, 'user_detail.html', {'musician': musician, 'requests': requests})

def request_detail(request, id):
    request1 = Request.objects.get(id=id)
    return render(request, 'request_detail.html', {'request1': request1})

def requests_view(request):
    requests = Request.objects.all()
    return render(request, 'requests.html', {'requests': requests})

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create_user(username=data['username'], password=data['password'])
            musician = Musician.objects.create(
                name = data['name'],
                teacher_or_student = data['teacher_or_student'],
                instruments_played = data['instruments_played'],
                bio = data['bio'],
                user = user
            )
            messages.success(request, 'Account successfully created!')
            return HttpResponseRedirect(reverse('home'))
    form = SignupForm()
    return render(request, 'student_signup.html', {'form': form})


def make_request(request):
    if request.method == "POST":
        form = RequestForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            request2 = Request.objects.create(
                name = data['name'],
                teacher_or_student = data['teacher_or_student'],
                text = data['text']
            )

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data['username'], password=data['password'])
            if user:
                login(request, user)
                messages.success(request, 'Login successful!')
                return HttpResponseRedirect(request.GET.get('next', reverse('home')))
            else:
                messages.error(request, 'Invalid username or password!')
        
    form = LoginForm()
    return render(request, 'login_form.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.success(request, 'Logout successful!')
    return HttpResponseRedirect(request.GET.get('next', reverse('home')))
