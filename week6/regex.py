#1
import re
p = r'a[b]*'
f = ['ab', 'abb', 'a', 'abc', 'aab']
for string in f:
    if re.search(p, string):
        print(f"{string} matches the sample.")
    else:
        print(f"{string} does not match the sample.")

#2
import re
p = r'a[b]{2,3}'
test = ['ab', 'abb', 'abbb', 'a', 'abc', 'aab']
for string in test:
    if re.search(p, string):
        print(f"{string} matches the sample.")
    else:
        print(f"{string} does not match the sample.")

#3
import re
p = r'[a-z]+_[a-z]+'
test = "this_is_a_test_of_programming_principle"
matches = re.findall(p, test)
print(matches)

#4
import re
p = r'[A-Z][a-z]+'
test = "This is a Test of Programming principle"
matches = re.findall(p, test)
print(matches)

#5
import re
p = r'a.*b$'
test = ['ab', 'acb', 'abcb', 'a', 'abc', 'aab']
for string in test:
    if re.search(p, string):
        print(f"{string} matches the sample.")
    else:
        print(f"{string} does not match the sample.")

#6
import re
p = r'[ ,.]'
test = "This is a test, of. Programming, principle, and 2."
str = re.sub(p, ':', test)
print(str)

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
pattern = r'[A-Z][^A-Z]*'
test = "ThisIsATestStringOfProgrammingPrinciple"
split_string = re.findall(p, test)
print(split_string)

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

def Camel_to_Snake(tet):
    p = re.compile(r'(?<!^)(?=[A-Z])')
    return p.sub('_', tet).lower()

tet = "camelCaseString"
result = Camel_to_Snake(tet)
print(result)




