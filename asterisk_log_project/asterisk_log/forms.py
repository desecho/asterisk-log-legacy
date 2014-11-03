# -*- coding: utf8 -*-
from django import forms
from datetime import datetime


# def convertToDatetime(date):
#     return datetime.strptime(date, "%d.%m.%Y").date()

regular_widget = forms.TextInput(attrs={'class': 'form-control'})


class CallForm(forms.Form):
    date = forms.DateField(label='Дата', required=False, widget=regular_widget)
    date_start = forms.DateField(label='Дата от', required=False, widget=regular_widget)
    date_end = forms.DateField(label='Дата по', required=False, widget=regular_widget)
    duration_from = forms.CharField(label='Длительность от', required=False, widget=regular_widget)
    duration_to = forms.CharField(label='Длительность по', required=False, widget=regular_widget)
    phone = forms.CharField(label='Телефон', required=False, widget=regular_widget)
    source = forms.CharField(label='Откуда', required=False, widget=regular_widget)
    destination = forms.CharField(label='Куда', required=False, widget=regular_widget)

    # def clean_date_start(self):
    #     return convertToDatetime(self.cleaned_data['date_start'])

    # def clean_date_end(self):
    #     return convertToDatetime(self.cleaned_data['date_end'])
