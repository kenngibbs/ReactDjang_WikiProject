from django import forms
from django.contrib.auth.models import User
from .models import MainWikiModel, RelatedWikiModel


class UserForm(forms.ModelForm):
    password = forms.PasswordInput()
    class Meta:
        model = User
        fields = ["username", "password"]

class MainWikiForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = MainWikiModel
        exclude = ["userForeignKey"]


class RelatedWikiForm(forms.ModelForm):
    relatedDescription = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = RelatedWikiModel
        exclude = ["mainForeignKey"]
