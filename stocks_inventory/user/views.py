from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm

# Create your views here.
def register(request):
    form= UserCreationForm
    context= {
        'form':form
    }
    return render(request, 'user/register.html', {'form':form})

def profile(request):
    return render(request, 'user/profile.html')