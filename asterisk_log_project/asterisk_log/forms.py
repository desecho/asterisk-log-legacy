# -*- coding: utf8 -*-
from django import forms
from datetime import datetime


# def convertToDatetime(date):
#     return datetime.strptime(date, "%d.%m.%Y").date()


class CallForm(forms.Form):
    date_start = forms.DateField(label='Дата от', required=False)
    date_end = forms.DateField(label='Дата по', required=False)
    duration_from = forms.CharField(label='Длительность от', required=False)
    duration_to = forms.CharField(label='Длительность по', required=False)
    source = forms.CharField(label='Откуда', required=False)
    destination = forms.CharField(label='Куда', required=False)

    # def clean_date_start(self):
    #     return convertToDatetime(self.cleaned_data['date_start'])

    # def clean_date_end(self):
    #     return convertToDatetime(self.cleaned_data['date_end'])
