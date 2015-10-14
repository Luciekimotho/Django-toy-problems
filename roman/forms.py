from django import forms

class RomanForm(forms.Form):
	roman_numeral = forms.CharField(label="Enter Roman Number")

