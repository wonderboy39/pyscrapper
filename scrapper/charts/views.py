# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import numpy as np


# Create your views here.
def index(request):
    template_data = {}
    print "index page..."
    return render(request, 'charts/index.html', template_data)


def render_chart(request):
    time_unit = [i for i in range(1,31)]
    data1 = np.random.randint(0, high=40, size=30).tolist
    data2 = np.random.randint(0, high=40, size=30).tolist

    template_data = {
        'day': [1,2,3],
        'temperature': [29,27,33],
        'time_unit': time_unit,
        'data1': data1,
        'data2': data2
    }
    if request.method == 'GET':
        print("get...")

    return render(request, 'charts/chart.html', template_data)