#!/usr/bin/env python3
"""
Author : cheny <cheny@localhost>
Date   : 2022-07-23
Purpose: Creating a class with 5 attributes for the instance level, 2 attribute for the class level and 5 methods
"""


class Car:

    # class attribute
    # promo discount using class attribute to achieve this discount

    pay_rate = 0.85  # pay rate after 15% discount has been made on each Audi car
    Increase = 1.10  # increasing the price of Audi car by 10%


# Method 1

    # the attributes for the instance level

    def __init__(self, name: str, price: float, distance_travelled: float, time: float, quantity=0):
        # Run validation to ensure no neagtive value is inputted for the attribute with float and integer value type

        assert price >= 0, f'price {price} is not greater than  or equals to zero!'
        assert distance_travelled >= 0, f'distance_travelled {distance_travelled} is not greater than or equals to zero!'
        assert time >= 0, f'time {time} is not greater than or equals to zero!'
        assert quantity >= 0, f'quantity {quantity} is not greater than or equals to zero!'

        # Assigning to self
        self.name = name
        self.price = price
        self.distance_travelled = distance_travelled
        self.time = time
        self.quantity = quantity
# Method 2

    def calculate_total_price(self):
        return self.price * self.quantity
# Method 3

    def speed(self):
        return self.distance_travelled / self.time
# Method 4

    def apply_discount(self):
        self.price = self.price * self.pay_rate
# Method 5

    def increament(self):
        self.price = self.price * self.Increase

# Instantiating the Object of the class Car


Audi = Car('Audi', 300000, 10, 2, 2)
print(Audi.calculate_total_price())
print(Audi.speed())
Audi.apply_discount()
print(Audi.price)
Audi.increament()
print(Audi.price)

Nissan = Car('Nissa', 250000, 6, 5, 4)
print(Nissan.calculate_total_price())
print(Nissan.speed())
Nissan.pay_rate = 0.9
Nissan.apply_discount()
print(Nissan.price)
