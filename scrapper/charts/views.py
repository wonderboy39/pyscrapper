# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


# Create your views here.
def index(request):
    template_data = {}
    print "index page..."
    return render(request, 'charts/index.html', template_data)


def render_chart(request):
    template_data = {
        'day': [1,2,3],
        'temperature': [29,27,33]
    }
    if request.method == 'GET':
        print("get...")

    return render(request, 'charts/chart.html',template_data)