from django.shortcuts import render
from .forms import RomanForm
# Create your views here.

def index(request):
	return render(request, 'index.html', {})

def romancode(request):
	form = RomanForm(request.POST or None)
	context = {
       "form": form
	}
	return render(request, 'romancode.html', context)
