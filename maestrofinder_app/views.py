from django.shortcuts import render, HttpResponseRedirect, reverse
from maestrofinder_app.models import Musician, Request
from maestrofinder_app.forms import StudentSignupForm, TeacherSignupForm, RequestForm, LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django import forms

# Create your views here.
def index_view(request):
    return render(request, 'index.html')

def profile_detail(request, id):
    musician = Musician.objects.get(id=id)
    requests = Request.objects.filter(musician=musician)
    return render(request, 'profile_detail.html', {'musician': musician, 'requests': requests})

def request_detail(request, id):
    request1 = Request.objects.get(id=id)
    return render(request, 'request_detail.html', {'request1': request1})

def add_request(request):
    if request.method == "POST":
        form = RequestForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            request2 = Request.objects.create(
                
            )
