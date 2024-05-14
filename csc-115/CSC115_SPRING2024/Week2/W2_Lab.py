import math

import random

# print("WEEK 2 LAB")

# phone_number = 3051234567
# area_code = phone_number // 10000000

# print(f"Area code is: {area_code}")

# phone = phone_number % 10000000

# print(f"The phone number is: {phone}")

# print(math.pi)
# print(f"The value of PI is {math.pi:.2f}")

# Activity 1 

# name = input("Enter your name: ")

# email = input("Enter your email: ")

# phone = input("Enter your phone: ")

# major = input("Enter your major: ")

# yearborn = int(input("Enter the year you were born: "))

# gpa = float(input("Enter your gpa: "))

# print(f"Name: {name} Email: {email} Phone: {phone} Major: {major} Yearborn: {yearborn} Gpa: {gpa}")

# Activity 2

# length = float(input("Enter the length: "))
# width = float(input("Enter the width: "))

# area = length * width

# perimeter = 2 * length + 2 * width

# print(f"Area: {area:.2f}") 
# print(f"Perimeter: {perimeter:.2f}")

# Activity 3

# radius = random.randint(1, 10)

# area = math.pi * radius ** 2

# circumference = 2 * math.pi * radius

# print(f"The radius: {radius:.2f}")

# print(f"Area: {area:.2f}")
      
# print(f"Circumference: {circumference:.2f}")

# Actvity 4

quarters = int(input("Enter the number of quarters: "))

dimes = int(input("Enter the number of dimes: "))

nickles = int(input("Enter the number of nickles: "))

pennies = int(input("Enter the number of pennies:"))



print(f"({quarters}*25 + {dimes}*10 + {nickles}*5 + {pennies}) / 100.0")

amount = (quarters * 25 + dimes * 10 + nickles * 5 + pennies) / 100.0
print(f"Amount : ${amount}")

