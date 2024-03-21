#!/bin/bash/env python
import phonenumbers
from phonenumbers import timezone,geocoder,carrier
number = input("Enter number with +63___: ")
phone=phonenumbers.parse(number)
time=timezone.time_zones_for_number(phone)
car=carrier.name_for_number(phone,"ph")
reg=geocoder.description_for_number(phone,"ph")
print(phone)
print(time)
print(car)
print(reg)
