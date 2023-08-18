#!/usr/bin/env python3

import ipdb

def admin_login(username, password):
    # your code here
    if (username == "admin" or username == "ADMIN") and password == "12345":
            return "Access granted"
    else:
        return "Access denied"
    

def hows_the_weather(temperature):
    # your code here
    if temperature < 40:
        return "It's brisk out there!"
    elif temperature > 40 and temperature < 65:
        return "It's a little chilly out there!"
    elif temperature > 85:
        return "It's too dang hot out there!"
    else:
        return "It's perfect out there!"

def fizzbuzz(num):
    # your code here
    #if (num / 3 == 1):
    #   print("Fizz")
    sum = num /3
    fum = num /5 
    if sum.is_integer() and fum.is_integer():
        return "FizzBuzz"
    elif fum.is_integer():
        return "Buzz"
    elif sum.is_integer():
        return "Fizz"
    else:
        return num

def calculator(operation, num1, num2):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        return num1 / num2
    else:
        print("Invalid operation!")
        return None 

#ipdb.set_trace()