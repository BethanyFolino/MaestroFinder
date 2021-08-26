from django.shortcuts import render, HttpResponseRedirect, reverse
from maestrofinder_app.models import Musician, Request
from maestrofinder_app.forms import AddProfileForm, RequestForm, LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django import forms

# Create your views here.
def index_view(request):
    return render(request, 'index.html')

