from django import forms as dfroms
from django.forms import fields

class UserForm(dfroms.Form):
    username = fields.CharField()
    email = fields.EmailField()