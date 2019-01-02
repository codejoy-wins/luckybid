# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Add Money to the users and subtract it for each bid.  

class User (models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    wins = models.IntegerField(default = 0)
    losses = models.IntegerField(default = 0)
    luckybucks = models.IntegerField(default = 0, null = True)
    created_at = models.DateTimeField(auto_now_add =True)
    updated_at = models.DateTimeField(auto_now=True)

class Product (models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(default="N/A", null=True)
    price = models.IntegerField(default = 0)
    category = models.CharField(default = "default", max_length=255)
    bidcount = models.IntegerField(default = 0, null=True)
    winner = models.CharField(default = "undecided", null=True, max_length=255)
    created_at = models.DateTimeField(auto_now_add =True)
    updated_at = models.DateTimeField(auto_now=True)

class Bid (models.Model):
    bidder = models.ForeignKey(User, related_name="bids", null=True)
    product = models.ForeignKey(Product, related_name="bids", null=True)
    created_at = models.DateTimeField(auto_now_add =True)
    updated_at = models.DateTimeField(auto_now=True)

    # if 0 wins and 100 losses, special promo item available

# keep track of who has a bid out for what

# product has related name winner for user
# user has related name products or bids for product