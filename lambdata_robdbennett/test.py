#!/usr/bin/env python
class Customer:
    def __init__(self, name, zip_code):
        self.name = name
        self.zip_code = zip_code

jane = Customer('Jane', 90210)

class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart
    def add(self, other_complex):
        self.r += other_complex.r
        self.i += other_complex.i

x = Complex(3.0, 2.0)

y = Complex(6.0, 4.2)

x.add(y)

class SocialMediaUser:
    def __init__(self, name):
        self.name = name
        self.upvotes = 0
    def receive_upvote(self):
        self.upvotes += 1
    def is_popular(self):
        return self.upvotes > 100
        
