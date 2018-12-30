# need to access request.Session and get an example going like request.SESSION['cat'] = "cookie"



# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from models import *

# Create your views here.
def index(request):
    request.session['cat'] = 'cookie'
    print request.session['cat']
    return render(request, "index.html")

def loginreg(request):
    print "loginreging"
    return render(request, "login.html")

def login(request):
    print "loggingin"
    if(request.POST['password'] == request.POST['confirm_password']):
        print 'MATCHED'
        User.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], address = request.POST['shipping_address'], email = request.POST['email'] , username = request.POST['username'], password = request.POST['password'])
        print "in db?"
        return redirect('/')

    else:
        print "NO MATCH"
        return redirect("/odell")

    # hey it works that's impressive

def loginreg2(request):
    print "loginreg2ing"
    return render(request, "login2.html")

def logintrue(request):
    try:
        current = User.objects.get(username = request.POST['username'])
    except:
        return redirect('/')
    if(current):
        if(current.password == request.POST['password']):
            print "password matches db"
            request.session['user_id'] = current.id
            print request.session['user_id']
            return redirect('/welcome')
        else:
            print "username and pw do not match database"
            return redirect('/odell')

            # logged on = true  need to log user on with session.
            # request.SESSION to log users on or off

def db(request):
    print User.objects.all()
    context = {
        'jay':'silent bob',
        'users': User.objects.all()
    }
    return render(request, "db.html", context)

def welcome(request):

    # redirect to home if not logged on

    print "welcoming"
    print request.session['user_id']
    superuser = User.objects.get(id=request.session['user_id'])
    context = {
        'jay': 'silent bob new',
        'me': request.session['user_id'],
        'you': superuser
    }
    return render(request, "welcome.html", context)

def logout(request):
    request.session.clear()
    print "logging out"
    return redirect('/odell')
def odell(request):
    return render(request, "odell.html")
