from django.conf.urls import url
from . import views


app_name = 'home'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^internprogramme/$', views.internprog, name='internprog'),
    url(r'^internshipapply/$', views.internapply, name='internapply'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^success/$', views.success, name='success'),
    url(r'^finance/$', views.finance, name='finance'),
    url(r'^trading/$', views.trading, name='trading'),
    url(r'^rpo/$', views.rpo, name='rpo'),
    url(r'^training/$', views.training, name='training'),
    url(r'^whatwedo/$', views.whatwedo, name='whatwedo'),
    ]
