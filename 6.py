#Python Sets 
#1
thisset = {"apple", "banana", "cherry"}
print(thisset)
#2
thisset = {"apple", "banana", "cherry"}

print(len(thisset))
#3
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

print(set1)
print(set2)
print(set3)
#4
set1 = {"abc", 34, True, 40, "male"}

print(set1)
#5
myset = {"apple", "banana", "cherry"}
print(type(myset))
#6
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)
#Access Set Items
#1
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)
#2
thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)
#3
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)
#4
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)
#5
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)

#Remove Set Items
#1
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)
#2
thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)
#3
thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)
#4
thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)
#5
thisset = {"apple", "banana", "cherry"}

del thisset

print(thisset)

#Loop Sets
#1
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

#Join Sets
#1
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)
#2
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)
#3
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x)
#4
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)

print(z)
#5
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

print(x)
#6
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

print(x)

#Set Methods
#add
fruits = {"apple", "banana", "cherry"}

fruits.add("orange")

print(fruits)
#2
fruits = {"apple", "banana", "cherry"}

fruits.add("apple")

print(fruits)

#clear
fruits = {"apple", "banana", "cherry"}

fruits.clear()

print(fruits)
#copy
fruits = {"apple", "banana", "cherry"}

x = fruits.copy()

print(x)
#difference
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.difference(y)

print(z)
#2
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = y.difference(x)

print(z)
#difference update
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.difference_update(y)

print(x)
#discard
fruits = {"apple", "banana", "cherry"}

fruits.discard("banana")

print(fruits)
#intersection
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)

print(z)
#2
x = {"a", "b", "c"}
y = {"c", "d", "e"}
z = {"f", "g", "c"}

result = x.intersection(y, z)

print(result)
#intersection update
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x)
#2
x = {"a", "b", "c"}
y = {"c", "d", "e"}
z = {"f", "g", "c"}

x.intersection_update(y, z)

print(x)
#isdisjoint
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}

z = x.isdisjoint(y)

print(z)
#issubset
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}

z = x.issubset(y)

print(z)
#issuperset
x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}

z = x.issuperset(y)

print(z)
#pop
fruits = {"apple", "banana", "cherry"}

fruits.pop()

print(fruits)
#remove
fruits = {"apple", "banana", "cherry"}

fruits.remove("banana")

print(fruits)
#symmetric_difference
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)

print(z)
#symmetric_difference_update
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

print(x)
#union
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.union(y)

print(z)
#2
x = {"a", "b", "c"}
y = {"f", "d", "a"}
z = {"c", "d", "e"}

result = x.union(y, z)

print(result)
#update
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.update(y)

print(x)


