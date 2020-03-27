from django.shortcuts import render,HttpResponse
from django.contrib.auth.forms import UserCreationForm
def home(request):
    return render(request,'accounts/home.html')

def signupst(request):
    return render(request,'accounts/signupst.html')

def signupmen(request):
    return render(request,'accounts/signupmen.html')

def aboutus(request):
    return render(request,'accounts/about.html')

def homein(request):
    return render(request,'accounts/homein.html')
def mentor(request):
    return render(request,'accounts/homein.html')
# path('password-change/', views.PasswordChangeView.as_view(), name='password_change'),
# path('password-change/done/', views.PasswordChangeDoneView.as_view(), name='password_change_done'),