print("WEEK 5 - LAB PRACTICE")

# # input_salary = float(input("Enter salary: "))
# # input_years_on_job = float(input("Enter years on job: "))

# # if (input_salary >= 30000 and input_years_on_job >= 2):
# #     print("You qualify for a loan.")
# # else:
# #     print("You do not qualify for a loan.")

# score = float(input("Enter score: "))

# if(score >= 90):
#     print("Your grade is A.")
# else:
#     if(score >= 80):
#         print("Your grade is B.")
#     else:
#         if(score >= 70):
#             print("Your grade is C.")
#         else:
#             if(score >= 60):
#                 print("Your grade is D.")
#             else:
#                 print("Your grade is F.")

# print('Here is the if- elif - else structure')

# if( score >= 90):
#     print("Your grade is A.")
# elif( score >= 80):
#     print("Your grade is B.")
# elif( score >= 70):
#     print("Your grade is C.")
# elif( score >= 60):
#     print("Your grade is D.")
# else:
#     print("Your grade is F.")

from datetime import date

yearBorn = int(input("When were you born? "))

age = date.today().year - yearBorn
print(age)
