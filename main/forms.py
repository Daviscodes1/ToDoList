from django import forms

class CreateNewList(forms.Form):
    name = forms.CharField(label="Name", max_length=500)
    check = forms.BooleanField(required=False)