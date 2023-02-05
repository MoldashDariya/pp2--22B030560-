#1
def my_fun():
    n = int(input())
    print(n/28,3495231)
my_fun()

#2
def my_temp():
    F = int(input())
    print((5/9) * (F - 32))
my_temp()


#3
def my_function():
    numheads = 35
    numlegs = 94
    a =(numlegs - (numheads*2))//2
    b=numheads - a
    print( a, b)
my_function()

#4
l = list(map(int, input().split()))
def filter_prime(l):
    if l == 0 or l == 1:
        return False
    for i in range(2, l // 2 + 1):
        if l % i == 0:
            return False
    return True

def check(l):
    for i in l:
        if filter_prime(i):
            print(i)


check(l)

#5
def permut(str, i=0):
    if i == len(str):
        print("".join(str))

    for j in range(i, len(str)):
        words = [c for c in str]

        # swap
        words[i], words[j] = words[j], words[i]

        permut(words, i + 1)


print(permut('yup'))


#6
w = input()
def palindrome(w):
    w1 = w[:: -1]
    print(w1)

palindrome(w)

#7
def has_33(l1):
    s = ""
    for i in l1:
        s += str(i)
    return "33" in s


print(has_33([1, 3, 3, 4]))


#8
def spy_game(name):
    for i in range (len(name)-2):
        if name[i] == "0" and name[i+1] == "0" and name[i+2] == "7":
            print("spy_game {} --> True".format(name))
        else:
            print("spy_game {} --> False". format(name))


name = [int(i) for i in input().split()]
spy_game(name)

#9
def my_sphere():
    r = int(input())
    print((4/3)*3.14 *r*r*r)
my_sphere()

#10
def func(l):
    x = []
    for a in l:

        if a not in x:
            x.append(a)

    return x


print(f([1, 2, 3, 3, 3, 3, 4, 5, 2]))


#11
s = input()


def palindrome(s):
    if s == s[:: -1]:
        return True
    return False


print(palindrome(s))


#12
def histogram():
    l = []
    n = int(input())
    for i in range(n):
        a = int(input())
        l.append(a)
        for i in range(n):
            print(l[i]*"*")
histogram()

#13
import random
guesses_made = 0
name = input("Hello! What is your name??\n")
number = random.randint(1, 20)
print ("Well,{} ,I am thinking of a number between 1 and 20.".format(name))
while guesses_made <20:
    guess = int(input('Number: '))
    guesses_made += 1
    if guess < number:
        print ("Your guess is too low.")

    if guess > number:
        print ("Your guess is too big.")

    if guess == number:
        print ("Good job, {0}!,You guessed my number in {1} guesses!".format(name, guesses_made))
        break
