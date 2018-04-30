# Python Intro

## Before you start
* Get Python 3 at [http://www.python.org].
* Get a decent Editor like [Sublimetext](https://www.sublimetext.com/).

## Things to keep in mind
* Whitespace is important in Python.
* Add this in front of every Python file: `# -*- coding: utf-8 -*`
* You can run Python programs directly in the Terminal by typing `python yourscript.py`. If you want to use Python 3 explicitly you need to type `python3 yourscript.py`.
* When you google Python tutorials, you will stumble upon something called "virtual environments" all the time. They are super handy and super important. But don’t stress yourself about them when you start learning Python.

## Basic syntax

In the beginning don’t hesitate to comment your code. You will thank yourself in the future.

```python
# This is a comment. You will see in the examples below, that you can use them inline.
```

### Variables
Variables are values you want to use later again. You won’t be able to live without them. Usually you should give them a declarative name, so you know what they mean.

```python
xyz = "hello" # You can either use `"`or `'` to declare strings.
abc = 'hello'
iam_a_number = 1
```

### Print
If you want to give the user feedback or see the content of certain variables at given moment, use `print()`.

```python
greeting = "hello"
print(greeting)

user = "Somebody"
print(greeting, user)
```

### If statements
Don’t do everything all the time. Do some stuff under certain conditions. Usually you use `==`/`is`, `!=`/`is not` to state the condition and `and` or `or` to combine them

```python
user = "Maik"

if user == "Maik":
    print("Hi Maik!")
else:
    print("Hallo", user)

if user is "Sven" or user is "Maria":
    print("Hey Sven or Maria")
```

### Lists
Lists can store multiple values. You can declare them in the list itself or store variables in them.

```python
somevar = "Teststring"
my_list = [1, "Hallo", somevar]
print(my_list)
```

### for loops
If you want to loop through a list, you use a for loop. After the `for` you declare a variable that is used within the loop for the values of the list.

```python
my_list = [1, "Hallo", somevar]

for this_val in my_list:
    print(this_val)
```

### Methods
Like variables for values, you can use methods for recurring things you want to do.

```python
def print_contents_of_list(input_list):
    for this_val in input_list:
        print(this_val)

my_list = [1, "Hallo", somevar]
my_other_list = ["Other", "Stuff"]
print_contents_of_list(my_list)
print_contents_of_list(my_other_list)
```