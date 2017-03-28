# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.shortcuts import render, redirect
import random
import re
from django.contrib import messages
from django.db.models import Count, DateTimeField
from models import *
import bcrypt

def index(request):
	context = {
		"Users": Users.objects.all(),
		}
	return render(request, 'wishexam/index.html', context)
def home(request):
	context = {
		"Users": Users.objects.all(),
		"curr_user": Users.objects.filter(id=request.session['userid']),
		"notwl": Items.objects.exclude(user_id__id=request.session['userid']).exclude(item_wl__wl_user=request.session['userid']),
		#"count": Quotes.objects.annotate(num_favs=Count('quote_favs')).order_by('num_favs'),
		"yourwl": Items.objects.filter(user_id__id=request.session['userid'])|Items.objects.filter(item_wl__wl_user=request.session['userid'])}
	return render(request, 'wishexam/home.html', context)
def selitem(request):
   	context = {
		"Users": Users.objects.all(),
		"curr_user": Users.objects.filter(id=request.session['userid']),
		"sel_item": Items.objects.filter(id=request.POST['selitem']),
		"users_item": Users.objects.filter(id=Users.objects.filter(user_wl__wl_item__item_wl__id=request.POST['selitem'])),
	}
	return render(request, 'wishexam/selitem.html', context)
def additem(request):
   	context = {
		"Users": Users.objects.all(),
		"curr_user": Users.objects.filter(id=request.session['userid']),

	}
	return render(request, 'wishexam/additem.html', context)	

def register(request): 

    if not request.POST['name']:
        messages.error(request, "Please enter your Name")
        return redirect("/")

    elif not request.POST['username']:
        messages.error(request, "Please enter an username")
        return redirect("/")
    elif Users.objects.filter(username=request.POST['username'])==True:
        messages.error(request, "username is already in use")
        return redirect("/")

    elif not request.POST['password']:
        messages.error(request, "enter a password")
        return redirect("/")
    elif len(request.POST['password']) < 8:
        messages.error(request, "Password must be at least 8 characters")
        return redirect("/")
    elif request.POST['password'] != request.POST["confirm"]:
        messages.error(request, "Password must match")
        return redirect("/")
    else:
        password = request.POST['password']
        hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        Key =Users.objects.create(name=request.POST['name'],dh=request.POST['dh'],username=request.POST['username'],pw_hash=hashed)
        request.session['userid'] = Key.id
        return redirect('/home')


def login(request):
    if not request.POST['username']:
    	messages.error(request, "Please enter your Username")
        return redirect("/")
    elif not Users.objects.filter(username=request.POST['username'])==True:
    	messages.error(request, "Not an existing Username")
    	return redirect("/")
    elif not request.POST['lgpassword']:
        messages.error(request, "Enter a password")
        return redirect("/")
    else:
	    Key = Users.objects.get(username=request.POST['username'])
	    storedhash = Key.pw_hash.encode('utf-8')
	    inputdata = bcrypt.hashpw(request.POST['lgpassword'].encode('utf-8'), storedhash)
	    if inputdata == storedhash:
	    	request.session['userid'] = Key.id
	    	print request.session['userid']
	        return redirect('/home')
	    else:
	        messages.error(request, "User name or password not valid Match")
	        return redirect('/')

def item(request):
    if len(request.POST['item']) < 4:
        messages.error(request, "Item must be more than 3 characters")
        return redirect("/additem")
    else:    
        Items.objects.create(item=request.POST['item'], added_by=request.POST['username'],user_id=Users.objects.get(id=request.session['userid']))
        return redirect('/home')

def wl(request):
    Wishlist.objects.create(wl_user=Users.objects.get(id=request.session['userid']),wl_item=Items.objects.get(id=request.POST['wish_this'])),
    return redirect('/home')
def removewl(request):
    Wishlist.objects.filter(wl_item=Items.objects.get(id=request.POST['unwish_this'])).delete()
    return redirect('/home')

def delete(request):
    print request.POST['delete_this']
    Items.objects.get(id=request.POST['delete_this']).delete()
    return redirect('/home')

def deleteuser(request):
    print request.POST['delete_this']
    Users.objects.get(id=request.POST['delete_this']).delete()
    return redirect('/')
def logout(request):
    request.session.clear()
    return redirect('/')