#!/usr/bin/env python3
# Raise salary by 5% if employee worked 
# for 5 or more years

service_years = int(input("How many year(s) have you worked here? "))
salary = int(input("Whats your net salary? "))
if service_years >= 5:
    salary += int(salary * 0.05)
print("Congratulations, you will start earing {} now".format(salary))
