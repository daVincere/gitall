# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from allauth import account_login, account_signup, account_logout


def loginView(request):

	