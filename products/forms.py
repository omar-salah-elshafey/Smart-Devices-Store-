from django import forms

from .models import PhoneRate, TabRate, AirpodRate, WatchRate


class PhoneForm(forms.ModelForm):
    class Meta:
        model = PhoneRate
        fields = ['name', 'email', 'body']


class TabForm(forms.ModelForm):
    class Meta:
        model = TabRate
        fields = ['name', 'email', 'body']


class AirpodForm(forms.ModelForm):
    class Meta:
        model = AirpodRate
        fields = ['name', 'email', 'body']


class WatchForm(forms.ModelForm):
    class Meta:
        model = WatchRate
        fields = ['name', 'email', 'body']
