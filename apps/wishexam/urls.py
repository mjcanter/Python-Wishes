# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^home$', views.home),
    url(r'^selitem$', views.selitem),
    url(r'^additem$', views.additem),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^item$', views.item),
    url(r'^wl$', views.wl),
    url(r'^removewl$', views.removewl),
    url(r'^delete$', views.delete),
    url(r'^deleteuser$', views.deleteuser),
    url(r'^logout$', views.logout),
    ]