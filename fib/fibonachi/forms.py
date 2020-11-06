from .models import Fibonachi
from django import forms
from django.forms import ModelForm


class FibForm(forms.ModelForm):
    class Meta:
        model = Fibonachi
        fields = ("number_input",)
