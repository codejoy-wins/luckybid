# need to access request.Session and get an example going like request.SESSION['cat'] = "cookie"

# how do I increase bidcount in db each time a bid is made?

# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from random import *

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

def db2(request):
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
    return render(request, "db2.html", context)

def welcome(request):

    # redirect to home if not logged on

    print "welcoming"
    print request.session['user_id']
    superuser = User.objects.get(id=request.session['user_id'])
    context = {
        'jay': 'silent bob new',
        'me': request.session['user_id'],
        'you': superuser,
        'bids': Bid.objects.all,
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

    if(the_user.luckybucks <= 0):
        print "out of cash"
        return redirect('/')
    print the_product.bidcount,  " is current bidcount"
    the_product.bidcount += 1
    print the_product.bidcount, " is now bidcount"
    the_product.save()

    print the_user.first_name, "is the user"
    print the_product.name, "is the product"
    print master_id, " is bidding on ", product_id
    Bid.objects.create(bidder=the_user, product =the_product)
    all_bids = Bid.objects.all()
    
    if the_product.bidcount >= 100:
        print "unacceptable2"
        winner = xp(all_bids)
        print winner.bidder.first_name, " is the winner!"
        the_product.winner = winner.bidder.first_name
        print the_product.winner, ' is product.winner'
        the_product.save()
    return redirect('/db')

def bid2(request, master_id, product_id):
    print "Bid2 Method"
    the_user = User.objects.get(id=master_id)
    if(the_user.luckybucks <= 0):
        print "out of cash"
        return redirect('/')
    the_product = Product.objects.get(id=product_id)
    print the_product.bidcount,  " is current bidcount"
    the_product.bidcount += 1
    # increase bid and decrease luckybucks
    the_user.luckybucks -= 1
    print the_product.bidcount, " is now bidcount"
    the_product.save()
    the_user.save()

    print the_user.first_name, "is the user"
    print the_product.name, "is the product"
    print master_id, " is bidding on ", product_id
    Bid.objects.create(bidder=the_user, product =the_product)
    all_bids = Bid.objects.all()
    
    if the_product.bidcount == 100:
        print "unacceptable2"
        winner = xp(all_bids)
        print winner.bidder.first_name, " is the winner!"
        the_product.winner = winner.bidder.first_name
        print the_product.winner, ' is product.winner'
        the_product.save()
    if the_product.bidcount >100:
        print "unacceptable1"
        the_product.bidcount-=1
        the_product.bidcount=100
        the_product.save()
        the_user.luckybucks+=1
        the_user.save()
    return redirect('/product/'+ product_id)

def xp(r):
    print r
    rando = randint(1,100)
    # change 42 to legit 1-100 later
    return r[rando]
    # this is function to pick random from 1-100

def productx(request,product_id):
    the_user = User.objects.get(id = request.session["user_id"])
    print "product xing"
    print product_id
    the_product = Product.objects.get(id=product_id)
    print the_product.winner, " is the product winner baby"
    context = {
        "product": the_product,
        "bids": Bid.objects.all(),
        "master": the_user,
    }
    return render(request, "productview.html", context)

def money(request):
    print "money function"
    the_user = User.objects.get(id=request.session['user_id'])
    the_user.luckybucks+=100
    the_user.save()
    return redirect('/')

def snap(request, user_id):
    print "snapping fingers"
    print user_id
    the_user = User.objects.get(id=user_id)
    the_user.delete()
    # idk how to delete user
    return redirect('/db')

def edit(request, user_id):
    print "editing", user_id
    the_user = User.objects.get(id=user_id)
    context = {
        'user': the_user,
    }
    return render(request,'edit.html', context)

def editing(request):
    print 'editing'
    the_user = User.objects.get(id=request.session['user_id'])
    print request.POST['address']
    print request.POST['email']
    the_user.email = request.POST['email']
    the_user.address = request.POST['address']
    the_user.save()
    return redirect('/')

def odell(request):
    return render(request, "odell.html")
