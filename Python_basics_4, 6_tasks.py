#Practical task 6.1 (subtract 5 days from the current date)

from datetime import datetime, timedelta
current_date = datetime.now()
print("Current date: ", str(current_date))
date_5days_ago = current_date - timedelta(days=5)
print("Date 5 days ago: ", str(date_5days_ago))

#Notes: MAKING CONSTANTS. You can make in other file

import constants as const
import datetime

current_date = datetime.date.today()
new_date = current_date - datetime.timedelta(days=const.DAYS_TO_SUBSTRACT)

print(const.DAYS TO SUBSTRACT, "days ago was: ", new_date)






#Practical task 4.1 (write function to find the Max of 3 numbers)

def max_functions():
    return max(9, 99, 999)
print(max_functions())


#Practical task 4.2 (write a program to reverse a string)

txt = "1234abcd" [::-1]
print(txt)

#Practical task 4.3 (write a function to calculate the sum of all numbers passed as its arguments)

def sum_numbers (*numbers:float) -> float:
    return (sum(numbers))
"""function calculates the sum of all numbers passed as its arguments"""
print(sum_numbers(1, 2, 3))
print(sum_numbers(8, 20, 2))
print(sum_numbers(12.5, 3.147, 98.1))
print(sum_numbers(1.1, 2.2, 5.5))





























