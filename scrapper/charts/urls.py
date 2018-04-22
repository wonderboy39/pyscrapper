from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^sample/$', views.render_chart, name='chart_sample')
]
