from django import forms
from django.contrib.auth.models import User
from maestrofinder_app.models import Musician, Request

class AddStudentForm(forms.Form):
    name = forms.CharField(max_length=100)
    teacher_or_student_choices = (
                (False, 'Student')
    )
    teacher_or_student = forms.ChoiceField(choices = teacher_or_student_choices, label='Teacher or Student', initial='', widget=forms.Select(), required=True)
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

class AddTeacherForm(forms.Form):
    name = forms.CharField(max_length=100)
    teacher_or_student_choices = (
                (True, 'Teacher')
    )
    teacher_or_student = forms.ChoiceField(choices = teacher_or_student_choices, label='Teacher or Student', initial='', widget=forms.Select(), required=True)
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

class AddProfileForm(forms.Form):
    name = forms.CharField(max_length=100)
    teacher_or_student_choices = (
                (True, 'Teacher'),
                (False, 'Student')
            )
    teacher_or_student = forms.ChoiceField(choices = teacher_or_student_choices, label='Teacher or Student', initial='', widget=forms.Select(), required=True)
    instruments_played = forms.CharField(widget=forms.Textarea)
    bio = forms.CharField(widget=forms.Textarea)

class RequestForm(forms.Form):
    name = forms.CharField(max_length=100)
    teacher_or_student_choices = (
                (True, 'Teacher'),
                (False, 'Student')
            )
    teacher_or_student = forms.ChoiceField(choices = teacher_or_student_choices, label='Teacher or Student', initial='', widget=forms.Select(), required=True)
    text = forms.CharField(widget=forms.Textarea)

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)