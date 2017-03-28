# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Users(models.Model):
	name = models.CharField(max_length=40)
	username = models.CharField(max_length=38)
	pw_hash = models.CharField(max_length=225)
	dh = models.DateField()
	created_at = models.DateTimeField(auto_now_add=True)

class Items(models.Model):
	item = models.CharField(max_length=40)
	added_by = models.CharField(max_length=40)
	created_at = models.DateTimeField(auto_now_add=True)
	user_id = models.ForeignKey(Users, related_name="user_quote")


class Wishlist(models.Model):
	wl_user = models.ForeignKey(Users, related_name="user_wl")
	wl_item = models.ForeignKey(Items, related_name="item_wl")
