# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class RiskField(models.Model):
    field_name = models.CharField(max_length=100, blank=False)
    field_type = models.CharField(
        choices=[
            ('text', 'text'),
            ('number', 'number'),
            ('date', 'date'),
            ('enum', 'enum')
        ],
        default='text',
        max_length=100
    )
    enum_choices = models.TextField(blank=True)
    default_value = models.CharField(max_length=100, blank=True)


class RiskType(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    risk_name = models.CharField(max_length=100, blank=False)
    risk_type = models.CharField(max_length=100, blank=False)
    risk_fields = models.ManyToManyField(RiskField)

    class Meta:
        ordering = ('created_at',)


class Risk(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    json_body = models.TextField(blank=False)

    class Meta:
        ordering = ('created_at',)
