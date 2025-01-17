# Print statements
print("Hello, world!")
print(3)

# Variable declaration and type checking
a = 5
print(a)
print(type(a))

b = "Michael"
print(b)
print(type(b))

# Checking types of various values
print(type(9.0))
print(type(True))

# Mathematical operations
c = 3
d = 4
e = 5
f = 6

g = c + d ** e / f % e
h = c - d / e ** f + d * c
print(h)

# Lists
l = [1, 2, 3, 5]
print(l[3])

n = [1, 2, 3, "five", 6.0]
print(n)

# String formatting
age = 5
print("My age is:", age)

st = "I am"
st1 = "not"
st2 = "years old"
st_f = "I am not {} years old"
st_not_f = "not"
print(st_f.format(st_not_f, age))
print(st, age, st2)
print(st_f)

# User input
age1 = input("Please enter your age: ")
print(age1)
print(type(age1))

# Future age calculation (example placeholder)
print("In 1 year, you will be {} years old".format(int(age1) + 1))
