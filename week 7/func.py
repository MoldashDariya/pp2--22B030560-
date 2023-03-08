#1
import math

num = [1, 2, 3, 4, 5, 6]

product = math.prod(num)
print(product)

#2
string = "Hello, This is Python program"

up = 0
low = 0

for char in string:
    if char.isupper():
        up += 1
    elif char.islower():
        low += 1


print("upper count: ", up)
print("lower count: ", low)

#3
def palindrome(string):
    string = ''.join(filter(str.isalnum, string.lower()))
    return string == string[::-1]


print(palindrome(input()))

#4
import math
import time

def squares(num, after):
    time.sleep(after / 1000.0)
    res = math.sqrt(num)
    return res

num = int(input())
after = int(input())

print(squares(num, after))

#5
def check(t):
    return all(t)

t = (True, True, True)

print(check(t))