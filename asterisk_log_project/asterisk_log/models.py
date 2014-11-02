# -*- coding: utf8 -*-

from django.db import models


class Call(models.Model):
    calldate = models.DateTimeField('дата/время звонка')
    src = models.CharField('откуда', max_length=80)
    dst = models.CharField('куда', max_length=80)
    duration = models.PositiveIntegerField('длительность')
