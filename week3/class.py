 #1
class Something:
    def _init_(self):
        self.string = ""

    def getString(self):
        self.string = input()

    def printString(self):
        print(self.string.upper())


string = Something()
string.getString()
string.printString()

#2
class Shape:
    def _init_(self):
        pass

    def area(self):
        return 0


class Square:
    def _init_(self, length=0):
        Shape._init_(self)
        self.length = length

    def area(self):
        return self.length * self.length


p = Square(4)
print(p.area())

#3
class Shape:
    def _init_(self, length):
        self.length = length

    def area(self):
        return self.length


class Rectangle(Shape):
    def _init_(self, length, weight):
        super()._init_(length)
        self.weight = weight

    def area(self):
        return super().area() * self.weight


p = Rectangle(2, 5)
print(p.area())

#4
import math

class Point:
    def _init_(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        return self.x, self.y

    def move(self, x, y):
        self.x += x
        self.y += y

    def distance(self, p1):
        a = p1.x - self.x
        b = p1.y - self.y
        return math.sqrt(a * 2 + b * 2)


p = Point(1, 2)
p2 = Point(3, 3)
print(p.show())
p.move(5, 6)
print(p.show())
print(p.distance(p2))

#5
class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdrawal(self, amount):
        if self.balance != 0 and self.balance >= amount:
            self.balance -= amount
        else:
            print("This sum cannot be given. Please try again.")
            return self.withdrawal(int(input()))


Mal = Account(input(), int(input()))
Mal.deposit(int(input()))
Mal.withdrawal(int(input()))

  
#6
l = [int(i) for i in input().split()]
primes=range(2,100000)
s = set()
s1 = set(l)
for i in range(2,len(l)):
    primes = filter(lambda x: x==i or x%i, primes)
    for j in primes:
        s.add(j)


print(*s.intersection(s1))
