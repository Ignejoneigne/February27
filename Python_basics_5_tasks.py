#Task1

a = "Igne"
b = "Hallo SheGoesTech"
print(a)
print(b)
print(a + b)

#Task5.1

for x in range(0, 101, 7):
    print(x)

#Task5.2
word = input("Enter a word: ")
averse = word[:]
reverse = word[::-1]
print(reverse)

word = input("Please input a word: ")
for x in range(len(word),-1, -1, -1):
    print(word[x], end="")
    print(x)



#Task5.2.1

def my_function(y):
    return y[::-1]
mytxt = my_function("task is done")
print(mytxt)

#Task5.3

import math
print(math.factorial(7))

#Task5.3.1

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
n=int(input("Input a number to compute the factorial :"))
print(factorial(n))


