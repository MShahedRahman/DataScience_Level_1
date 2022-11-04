

# 1.1 learn about data types
a = 10  # integer
print(a)
b = 10.05  # float
c = 'python'  # string
d = [1, 3, 4, 6, 7, 10, 'sakib']  #list
e = {'key1' : [100, 105, 106], 'key2': 'value2'}  # dictionaries
e1 = { 'students' : ["abrar","raita", "kamal"],
     'class': "first class"}

print(d)

# associative array, e, dict  
f = (1,2,3,4)  # tuple

print(a)
print(type(a),type(b))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))

print(a, b)
print("first value: ", a, "second value:", b)
print(c)
print(d)
print(d)
print(e)
print(f)
#%%

# 1.2 learn about Operators

# 1.2.1 arithmetic operators

# addition
a = 5
b = 10
c = a + b
print(c)

# substruction
a = 50
b = 10
c = a - b
print(c)

# multiplication
a = 20
b = 10
c = a * b
print(c)

# division
a = 50
b = 10
c = a / b
print(int(c))

# modulo/reminder
p = 11
q = 3
r = p % q
print(r)

# exponent
a = 2
b = 3
c = a**b
print(c)

#%%
# 1.2.2 Comparison Operator

# Greater than

a = 8
b = 9

print(b > a)

# grater than or equal to
print(a >= b)

# less than or equal to
print(a <= b)

# equal to
print(a == b)

# NOT equal to
a = 8
b = 9
c = (a != b)
print(c)

#%%
# 1.2.3 Assignment Operators

a = 5
b = 10

# a = a + b
a += b
print(a)
#print(c)

a -= b  # a =  a - b
print(a)

#a += b
a *= b  
print(a)

#a += b
a /= b  
print(a)
#%%

# 1.3 Strings

string = "hello world!"
print(string)

# 1.3.1 Methods of String

# length
print(len(string))

# index
print(string[6])

# multiple strings
s = [ "Our first class", "thursday", "sakib", "internt",'python', 'sakib', 'tasmia', 'hasan', 'imtiaz', 'tayem' ]
#print(s)

#print(len(s))


# Slicing 
print(string[2:])

print(string[:11])

print(string[:])

# from backword
print(string[-1])  # only last value

print(string[ :-1])  # all except last value

# interval/frequency
print(string[::2])

# reverse
print(string[::-1])

# as
print(string[1:7])

#%%
# concatanate
s = "hello world"
a = " to all of us"
s = s + a
#print(s)

# capitalize
#print(s.upper())

m2 = "RUHIT"
#print(m2.lower())

# Skip split
print(s.split("o"))


# count
print(s.count("l"))

print(s.isalnum())

print(s.isdigit())

# finding an item/index
print(s.find("r"))

#%%
# class ends here