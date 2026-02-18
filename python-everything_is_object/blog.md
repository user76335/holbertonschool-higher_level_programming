Everything Is Object in Python

Introduction
In this project from the python-everything_is_object directory of the holbertonschool-higher_level_programming repository, I explored one of Python’s most fundamental truths: everything is an object. Variables don’t store values directly — they store references to objects in memory. Understanding this concept is crucial to writing clean, bug-free Python code, especially when dealing with mutable objects and function arguments.

id and type
Every object in Python has:


A type


An identity


A value


The identity of an object is its memory address in CPython. You can access it using:
x = 42
print(id(x))
print(type(x))

Example output:
9794400
<class 'int'>

The id() function returns the memory address of the object. The type() function tells us what kind of object it is.
If two variables point to the same object:
a = 89
b = 89

print(id(a))
print(id(b))
print(a is b)

Output:
140737488346512
140737488346512
True

Small integers are cached, so Python reuses the same object.

Mutable Objects
Mutable objects can change after creation.
Examples:


lists


dictionaries


sets


Example:
l1 = [1, 2, 3]
l2 = l1

l1.append(4)

print(l1)
print(l2)

Output:
[1, 2, 3, 4]
[1, 2, 3, 4]

Both changed because both variables reference the same object.
However:
l1 = [1, 2, 3]
l2 = l1

l1 = l1 + [4]

print(l2)

Output:
[1, 2, 3]

Here, l1 + [4] creates a new object, and l1 now points to a different list.

Immutable Objects
Immutable objects cannot change after creation.
Examples:


int


float


str


tuple


Example:
a = 89
b = a
a = a + 1

print(b)

Output:
89

When a becomes 90, Python creates a new object instead of modifying 89.
With strings:
s1 = "Best School"
s2 = "Best School"

print(s1 == s2)
print(s1 is s2)

Output:
True
True

Python often interns identical string literals, so they may share the same memory.

Why Does It Matter?
Understanding mutable vs immutable objects prevents subtle bugs.
Example bug:
def add_item(my_list=[]):
    my_list.append(1)
    return my_list

print(add_item())
print(add_item())

Output:
[1]
[1, 1]

Why? Because default mutable arguments are created once and reused.
This is why best practice is:
def add_item(my_list=None):
    if my_list is None:
        my_list = []
    my_list.append(1)
    return my_list


How Arguments Are Passed to Functions
Python uses pass-by-object-reference.
Example with immutable:
def increment(n):
    n += 1

a = 10
increment(a)
print(a)

Output:
10

The integer cannot be modified in place.
Example with mutable:
def add_item(lst):
    lst.append(4)

l = [1, 2, 3]
add_item(l)
print(l)

Output:
[1, 2, 3, 4]

The original list is modified because the function receives a reference to the same object.

Advanced Lessons Learned
From the deeper exercises, I learned:


is compares identity.


== compares value.


Small integers and some strings are interned.


+= behaves differently for mutable vs immutable objects.


Assignment never copies objects — it only binds names to objects.


Example:
a = [1, 2]
b = a
a += [3]
print(b)

Output:
[1, 2, 3]

But:
a = (1, 2)
b = a
a += (3,)
print(b)

Output:
(1, 2)

Lists mutate. Tuples create new objects.

Final Thoughts
Understanding how Python handles objects, memory, mutability, and identity is foundational to mastering the language. The phrase “everything is an object” isn’t just theory — it explains why certain bugs happen and how to avoid them.
Once you truly understand references, identity, and mutability, Python becomes much more predictable — and much more powerful.
