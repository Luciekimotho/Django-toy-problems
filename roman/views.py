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

	if form.is_valid():
		roman_numeral = form.cleaned_data.get('roman_numeral')
		translated = translate(roman_numeral)

	return render(request, 'romancode.html', context)



def translate(myroman):
    myDict = {
      'I': 1,
      'V': 5,
      'X': 10,
      'L': 50,
      'C': 100 }

    myroman = myroman.upper()
    number = 0
    while myroman:
        if len(myroman) == 1 or myDict[myroman[0]] >= myDict[myroman[1]]:
            number += myDict[myroman[0]]
            myroman = roman[1:]
        else:
            number += myDict[myroman[1]] - myDict[myroman[0]]
            myroman = myroman[2:]
    print (number)
