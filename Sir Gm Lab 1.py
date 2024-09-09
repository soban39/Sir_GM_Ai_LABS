# Input/output
text="i am Husnain Ali";
print(text);

# Multiple statements on a single line
print("statement1");print("statement2")

# Indentation with Tab space
x=1
if x>0:
    print("This statement has indentation")
# Identation with sinle space
x=1
if x>0:
 print("This statement has indentation")
# Identation with tab+single space
x=1
if x>0:
    print("This statement has indentation")

# Assigning integer values
a = 1452
print(type(a))  # <class 'int'>

b = -4587
print(type(b))  # <class 'int'>

c = 0
print(type(c))  # <class 'int'>

# Assigning float values
g = 1.03
print(type(g))  # <class 'float'>

h = -11.23
print(type(h))  # <class 'float'>

i = .34
print(type(i))  # <class 'float'>

j = 2.12e-10
print(type(j))  # <class 'float'>

k = 5E220
print(type(k))  # <class 'float'>

# Creating a complex number
x = complex(1, 2)
print(type(x))  # <class 'complex'>
print(x)  # Output: (1+2j)

# Performing addition with complex numbers
y = 1 + 2j
print(y)  # Output: (1+2j)
z = 1 + y
print(type(z))  # <class 'complex'>
print(z)  # Output: (2+2j)

# Creating boolean values
x = True
print(type(x))  # <class 'bool'>
print(x)  # Output: True
y = False
print(type(y))  # <class 'bool'>
print(y)  # Output: False

# Performing actions on strings
string1="Python TUTORIAL"
print(string1[0])
print(string1[-15])
print(string1[7])

# List indices
my_list1=[5,6,7,8,9,100]
my_list2=['red','orange','white','black']
my_list3=['Violet',100,121.12]
print(my_list1[2])
print(my_list2[1:-2])
print(my_list3[:3])


