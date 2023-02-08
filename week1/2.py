# many values to multiple variables
x = y = "world"
print(x)
print👍
print(x, y)

# collection/list
names = ["alan", "aziza", "roman"]
a, b, c = names
print(a)
print(b)
print(c)

# output variables
d = "welcome"
e = "to"
f = "pp2"
print(d, e, f)
# print(d + e + f) - without whitespaces
print(d + " " + e + " " + f)

# mathematical operators
m = 5
n = 15
print(m + n)
print(m * n)
print(n / m)
print(n % m)
print(n ** m)

# function
g = "Ok"

def myfunc():
    print("Python is " + g)

myfunc()

# number types
x = 5        # int
y = "Alan"   # str
z = 20.5     # float
a = True     # bool
b = 1j       # complex
print(type(x))
print(type(y))
print(type(z))
print(type(a))
print(type(b))

# type conversion
a = 5
b = 3.6
c = 1j

d = float(a)    # from int to float
e = int(b)      # from float to int
f = complex(a)  # from int to complex

print(d)
print(e)
print(f)

# random
"""import random
    print(random.randrange(1,10))"""