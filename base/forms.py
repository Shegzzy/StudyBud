from dataclasses import field, fields
from pyexpat import model
from django.forms import ModelForm
from .models import Room
from django.contrib.auth.models import User


class roomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['host', 'participants']


class UpdateUser(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
