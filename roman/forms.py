from django import forms

class RomanForm(forms.Form):
    roman_numeral = forms.CharField(widget=forms.TextInput(), label="Input roman numeral")

def clean_sent(self):
	roman_numeral = self.cleaned_data.get('roman_numeral')
	if roman_numeral == "":
		raise form.ValidationError("Cant be null")
	print (roman_numeral)
	return roman_numeral
