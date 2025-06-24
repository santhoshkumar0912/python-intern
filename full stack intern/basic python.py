#1
x = 5
y="John"
print(x)
print(y)

#2
x = 4
x="Sally"
print(x)

#3
x = str(3)
y=int(3)
z=float(3)
print(x)
print(y)
print(z)

#4
x = 5
y = "John"
print(type(x))
print(type(y))

#5
a = 4
A="Sally"
print(a)
print(A)

#6
x,y,z="Orange", "banana","cherry"
print(x)
print(y)
print(z)

#7
x=y=z="Orange"
print(x)
print(y)
print(z)

#8
fruits=["apple","banana","cherry"]
x,y,z=fruits
print(x)
print(y)
print(z)

#9
x="Python"
y="is"
z="awesome"
print(x,y,z)

#10
x=5
print(type(x))
print(x)

#11
x=1
y=2.8
z=1j
print(type(x))
print(type(y))
print(type(z))

#12
x=1
y=35656222554887711
z=-3255522
print(type(x))
print(type(y))
print(type(z))

#13
x=1.10
y=1.0
z=-35.59
print(type(x))
print(type(y))
print(type(z))

#14
x=3+5j
y=5j
z=-5j
print(type(x))
print(type(y))
print(type(z))

#15
x=1
y=2.8
z=1j
a=float(x)
b=int(y)
c=complex(x)
print(a)
print(b)
print(c)

#16
x=int(1)
y=int(2.8)
z=int("3")
print(x)
print(y)
print(z)

#17
x=float(1)
y=float(2.8)
z=float("3")
w=float("4.2")
print(x)
print(y)
print(z)
print(w)

#18
x=str("s1")
y=str(2)
z=str(3.0)
print(x)
print(y)
print(z)

#19
a="Hello"
print(a)

#20
a="""Lorem ipsum dolor sit amet,consectetur adipiscing elit,sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."""
print(a)

#21
a="Hello, world!"
print(a[1])

#22
for x in "banana":
  print(x)

#23
a="Hello,World!"
print(len(a))

#24
txt="The best things in life are free!"
print("free" in txt)

#25
txt="The best things in life are free!"
if"free"in txt:
  print("Yes,'free'is present")

#26
txt="The best things in life are free!"
print("expensive" not in txt)

#27
b="Hello, World!"
print(b[2:5])

#28
a=b="Hello, World!"
print(b[:5])
print(b[2:])
print(b[-5:-2])
print(a.upper())
print(a.lower())

#29
a="Hello, World!"
print(a.strip())
print(a.replace("H","J"))
print(a.split(","))

#30
a="Hello"
b="World"
c=a + b
print(c)

#31
print(10>9)
print(10==9)
print(10<9)

#32
a=200
b=33
if b>a:
  print("b is greater than a")
else:
  print("b is not greater than a")

#33
print(bool("Hello"))
print(bool(15))

#34
mylist=["apple","banana","cherry"]
print(mylist)

#35
thislist=["apple","banana","cherry"]
print(thislist)

#36
list1=["apple","banana","cherry"]
list2=[1,5,7,9,3]
list3=[True,False,False]
print(list1)
print(list2)
print(list3)

#37
list1=["abc",34,True,40,"male"]
print(list1)

#38
mylist=["apple","banana","cherry"]
print(mylist)

#39
thislist=list(("apple","banana","cherry","orange","kiwi","melon","mango"))
print(thislist[1])
print(thislist[-1])
print(thislist[2:5])
print(thislist[:4])
print(thislist[-4:-1])

#40
thislist=["apple","banana","cherry"]
thislist.append("orange")
print(thislist)
thislist.insert(1,"orange")
print(thislist)
thislist.remove("banana")
print(thislist)
for x in thislist:
  print(x)
  for i in range(len(thislist)):
    print(thislist[i])

#40
mytuple=("apple","banana","cherry")
thistuple=("apple","banana","cherry")
print(thistuple)
print(thistuple[-1])
print(thistuple[1])

#41    
thistuple=("apple","banana","cherry","orange","kiwi","melon","mango")
print(thistuple[:4])

#42
myset={"apple","banana","cherry"}
thisset={"apple","banana","cherry"}
print(thisset)

#43
thisset={"apple","banana","cherry",True,1,2}
print(thisset)
thisset=("apple","banana","cherry")
print(thisset)

#44
set1={"apple","banana","cherry"}
set2={1,5,7,9,3}
set3={True,False,False}
print(set1)
print(set2)
print(set3)

#45
set1={"abc,34,True,40,male"}
print(set1)

#46
thisset={"apple","banana","cherry"}
for x in thisset:
  print(x)

#47
set1={"a","b","c"}
set2={1,2,3}
set3=set1.union(set2)
print(set3)

#48
set1={"a","b","c"}
set2={1,2,3}
set3=set1|set2
print(set3)

#49
set1={"a","b","c"}
set2={1,2,3}
set3={"John","Elena"}
set4={"apple","banana","cherry"}
myset=set1.union(set2,set3,set4)
print(myset)

#50
thisdict={
    "brand":"Ford",
    "model":"Mustang",
    "year":1964
}
print(thisdict)
print(thisdict["brand"])

#51
thisdict=dict(name="John",age=36,country="Norway")
print(thisdict)

#52
a=33
b=200
if b>a:
  print("b is greater than a")

#53
i=1
while i<6:
  print(i)
  i+=1

#54
fruits=["apple","banana","cherry"]
for x in fruits:
  print(x)

#55
fruits=["apple","banana","cherry"]
for x in fruits:
  print(x)
  if x=="banana":
    break

#56
for x in range(6):
  print(x)

#57
for x in range(2,30,3):
  print(x)

#58
for x in range(2,6):
  print(x)

#59
def my_function(fname):
  print(fname)
my_function("hello from a function")

#60
def my_function(fname):
  print(fname+"Refsnes")
my_function("Emil")
my_function("Tobias")
my_function("Linus")

#70
def my_function(fname,lname):
  print(fname+" "+lname)
my_function("Emil","Refsnes")

#71
name=input("Enter your name:")
print(f" hello{name}")

#72


def myfunc():
  global x
  x=300

myfunc()

print(x)

#73
x=300
def myfunc():
  x=200
  print(x)

myfunc()

print(x)

#74
x=300
def myfunc():
  print(x)

myfunc()

print(x)

#75
def myfunc():
  x=300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()

#76
def myfunc():
  x = 300
  print(x)

myfunc()

#77
class Person:
  def __init__(self,name,age):
    self.name=name
    self.age=age
p1=Person("John",36)
print(p1.name)
print(p1.age)

