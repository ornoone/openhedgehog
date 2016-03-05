#!/bin/env python3
# -*- coding: utf-8 -*-
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _

__author__ = 'darius BERNARD <darius@xornot.fr>'
from django.db import models
import logging

logger = logging.getLogger(__name__)

# Create your models here.

class Bank(models.Model):
    name = models.CharField(_("name"))

    class Meta:
        verbose_name = _('bank')
        verbose_name_plural = _('banks')

class Household(models.Model):
    users = models.ManyToManyField(to=get_user_model(), verbose_name=_("users"))

    class Meta:
        verbose_name = _('household')
        verbose_name_plural = _('households')


class Account(models.Model):
    bank = models.ForeignKey(to=Bank, verbose_name=_("bank"), on_delete=models.PROTECT)
    household = models.ForeignKey(to=Household, verbose_name=_("household"), on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('account')
        verbose_name_plural = _('accounts')

class Balance(models.Model):
    account = models.ForeignKey(to=Account, verbose_name=_("account"))
    date = models.DateTimeField(_("date"), auto_now=True)
    amount = models.DecimalField(_("amount"))

    class Meta:
        verbose_name = _("balance")
        verbose_name_plural = _("balances")


CATEGORY_TYPE = [
    ("recurrent", _("recurrent")),
    ("exceptional", _("exceptional")),
    ("variable", _("variable")),
]


class Category(models.Model):
    name = models.CharField(_("name"))
    category_type = models.CharField(_("name"), choices=CATEGORY_TYPE)


MEANS = [
    ("CHECK", _("check")),
    ("CACH", _("cash")),
    ("TRANSFER", _("transfer")),
    ("CARD", _("bank card")),
]

CURRENCY = [
    ("EUR", "€"),
]


class Entry(models.Model):
    amount = models.DecimalField(_("amount"), decimal_places=2, max_digits=14)
    account = models.ForeignKey(to=Account, verbose_name=_("account"), on_delete=models.CASCADE)
    date_created = models.DateTimeField(_("date of creation"), auto_now_add=True)
    date_modification = models.DateTimeField(_("date of modification"), auto_now=True)
    date_value = models.DateTimeField(_("date of value"), auto_now_add=True)
    label = models.CharField(_("label"), max_length=255, blank=True, default="")
    comment = models.TextField(_("comment"), blank=True, default="")
    reference = models.CharField(_("reference of the existing piece"), blank=True,  default="")
    mean_of_payment = models.CharField(_("mean of payment"), max_length=32, choices=MEANS)
    currency = models.CharField(_("currency"), max_length=3, choices=CURRENCY, default=CURRENCY[0][0])


    class Meta:
        verbose_name = _('entry')
        verbose_name_plural = _('entrys')


class Budget(models.Model):
    pass