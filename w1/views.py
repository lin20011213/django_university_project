# -*- coding: utf-8 -*-
from django.http import HttpResponse

def here(request):
    return HttpResponse('Mom, I am here!')
