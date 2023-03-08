#1
import os

path = '/Users/MoldashDariya/VisualStudioCode/pp2-22B030560/lab4'


print("Directories:")
for i in os.listdir(path):
    if os.path.isdir(os.path.join(path, i)):
        print(i)


print("\nFiles:")
for file in os.listdir(path):
    if os.path.isfile(os.path.join(path, file)):
        print(file)


print("\nAll directories and files:")
for all in os.listdir(path):
    print(all)

#2
import os

path = '/Users/MoldashDariya/VisualStudioCode/pp2-22B030560/lab5/file.txt'

if os.access(path, os.F_OK):
    print("yes, it exists")
else:
    print("no, it doesn't exist")

if os.access(path, os.R_OK):
    print("yes, readable")
else:
    print("no, can't read")

if os.access(path, os.R_OK):
    print("yes, writable")
else:
    print("no, can't write")

if os.access(path, os.X_OK):
    print("yes, can execute")
else:
    print("no, can't")

#3
import os
path = '/Users/MoldashDariya/VisualStudioCode/pp2-22B030560/lab6/dir'

if os.access(path, os.F_OK):
    print("exists")
    print(os.path.basename(path))
    print(os.path.dirname(path))
else:
    print("doesn't exist")


# if os.path.exists(path):
#     print(f'{path} exists')
#     print(os.path.basename(path))
#     print(os.path.dirname(path))
# else:
#     print(f'{path} does not exist')

#4
import os

path = '/Users/MoldashDariya/VisualStudioCode/pp2-22B030560/lab5/file.txt'
with open(path, 'r') as f:
    cnt = 0
    for line in f:
        cnt += 1

print(cnt)

#5
list = ['hello', ',', 'this', 'is', 'lab', 'work', 'number', 'six']

path = input("name: ")


with open(path, 'w') as file:

    for s in list:
        file.write(s + ' ')


print("The list is in the file ", path)

#6
import os
import string

alphabet = 'files'
if not os.path.exists(alphabet):
    os.makedirs(alphabet)

for l in string.ascii_uppercase:
    name = os.path.join(alphabet, l + '.txt')

    with open(name, 'w') as f:
        pass

    print("done!")

#7
import os

first = 'first.txt'
second = 'second.txt'
with open(first, 'r') as f:
    x = f.read()

with open(second, 'w') as n:
    n.write(x)

print("done!")

#8
import os

path = '/Users/MoldashDariya/VisualStudioCode/pp2-22B030560/lab6/dir/test.py'

if os.path.exists(path)and os.access(path, os.F_OK):
    os.remove(path)
    print("done!")
else:
    print("file does not exist")

