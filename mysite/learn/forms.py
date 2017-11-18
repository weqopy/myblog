from django import forms


class LearnForm(forms.Form):
    a = forms.IntegerField()
    b = forms.IntegerField()
