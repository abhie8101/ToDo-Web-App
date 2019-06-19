from .models import todomodel
from django.db import models
from django import forms

class todoform(forms.ModelForm):

    class Meta():
        model = todomodel
        fields = ('Title','Discription')
