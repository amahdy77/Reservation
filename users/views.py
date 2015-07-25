from django.shortcuts import render
from .models import ExpectedUser

# Create your views here.

def home(request):
    all_data = ExpectedUser.objects.all()
    context = {
        'all_data': all_data
    }
    return render(request, 'index.html', context)