#1
import re
with open('original.txt', 'r', encoding = "utf-8") as f:
    text = f.read()


pattern = r'a(b*)'
pattern1 = r'а(б*)'

matches = re.findall(pattern, text)
matches1 = re.findall(pattern1, text)
print(matches, matches1)

#2
import re
with open('original.txt', 'r', encoding = "utf-8") as f:
    text = f.read()

pattern = r'a(bb|bbb)'
pattern1 = r'а(бб|ббб)'

matches = re.findall(pattern, text)
matches1 = re.findall(pattern1, text)
print(matches, matches1)

#3
import re
with open('original.txt', 'r', encoding = "utf-8") as f:
    text = f.read()


pattern = r'[a-z]+_[a-z]+'
pattern1 = r'[а-я]+_[а-я]+'

matches = re.findall(pattern, text)
matches2 = re.findall(pattern1, text)
print(matches, matches2)

#4
import re
with open('original.txt', 'r', encoding = "utf-8") as f:
    text = f.read()


pattern = r'[A-Z][a-z]+'
pattern1 = r'[А-Я][а-я]+'

matches = re.findall(pattern, text)
matches2 = re.findall(pattern1, text)
print(matches, matches2)

#5
import re
with open('original.txt.txt', 'r', encoding = 'utf-8') as f:
    text = f.read()


pattern = r'a.+b$'
pattern1 = r'а.+б$'

matches = re.findall(pattern, text)
matches2 = re.findall(pattern1, text)
print(matches)
print(matches2)

#6
import re

with open('file.txt', 'r', encoding = "utf-8") as f:
    txt = f.read()

new = re.sub(r'[ ,.]', ':', txt)

with open('file.txt', 'w') as f:
    f.write(new)

#7
def snake_to_camel(snake_str):
    comp = snake_str.split('_')
    return comp[0] + ''.join(x.title() for x in comp[1:])

# example 
snake_str = "my_snake_case_string"
camel_str = snake_to_camel(snake_str)
print(camel_str)

#8
import re
txt = "PythonProgram"
def split(s):
    x = re.findall('[A-Z][^A-Z]*', txt)
    return " ".join(x)


print(split(txt))

#9
import re

def insert_Spaces(tet):
    p = r"(\b[A-Z][a-z]+\b)"
    return re.sub(p, r" \1", tet)

tet = "ThisIsATestStringOfProgrammingPrinciple"
result = insert_Spaces(tet)
print(result) 

#10
import re

s = "CamelCaseString"
def camel(s):
    pattern = re.compile(r'(?<!^)(?=[A-Z])')
    snake = pattern.sub('_', s).lower()
    return snake


print(camel(s))