# need to access request.Session and get an example going like request.SESSION['cat'] = "cookie"



# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from models import *

# Create your views here.
def index(request):
    if 'user_id' in request.session:
        print 'id in sesh already'
        return redirect('/welcome')

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
        the_user = User.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], address = request.POST['shipping_address'], email = request.POST['email'] , username = request.POST['username'], password = request.POST['password'])
        print "in db?"
        request.session['user_id'] = the_user.id
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
    print Product.objects.all()
    if not 'user_id' in request.session:
        print 'no id in sesh'
        return redirect('/')
    print request.session['user_id'], "is user id in sesh"
    context = {
        'jay':'silent bob',
        'bids': Bid.objects.all(),
        'users': User.objects.all(),
        'products': Product.objects.all(),
        'master': User.objects.get(id=request.session['user_id']),
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
    return redirect('/')

def product(request):
    print "product UI"
    return render(request, "product.html")

def addproduct(request):
    print "adding product"
    print request.POST['name']
    suzy = Product.objects.create(name=request.POST['name'], description=request.POST['description'], price = request.POST['price'], category = request.POST['category'])
    print suzy.name ,"is suzys name"
    return redirect("/product")

def destroy(request, product_id):
    print "Destroy view"
    print product_id
    Product.objects.get(id=product_id).delete()
    return redirect('/db')

def bid(request, master_id, product_id):
    print "Bid Method"
    the_user = User.objects.get(id=master_id)
    the_product = Product.objects.get(id=product_id)
    print the_user.first_name, "is the user"
    print the_product.name, "is the product"
    print master_id, " is bidding on ", product_id
    Bid.objects.create(bidder=the_user, product =the_product)
    return redirect('/db')

def odell(request):
    return render(request, "odell.html")
