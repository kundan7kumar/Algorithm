# Arithmetic operators
"""
+ Addition
- Subtraction
* Multiplication
/ Division
% Mod (the remainder after dividing)
** Exponentiation (note that ^ does not do this operation, as you might have seen in other languages)
// Divides and rounds down to the nearest integer

Pythonic Way= all letter should be small separated with _
nly use ordinary letters, numbers and underscores in your variable names. They can’t have spaces, and need to start with a letter or underscore.
You can’t use reserved words or built-in identifiers
The pythonic way to name variables is to use all lowercase letters and underscores to separate words.
The way we name variables is called snake case, because we tend to connect the words with underscores.
Below are the assignment operators from the video. You can also use *= in a similar way, but this is less common than the operations shown below. You can find some practice with much of what we have already covered here.

Note that this code uses scientific notation to define large numbers. 4.445e8 is equal to 4.445 * 10 ** 8 which is equal to 444500000.0
"""

#x, y, z =2, 3, 4

car = 24
rabb = 8
crs_per_rab = car/rabb
rabb = 12
print(crs_per_rab)

Integers and Floats
There are two Python data types that could be used for numeric values:

int - for integer values
float - for decimal or floating point values
x = int(4.7)   # x is now an integer 4
y = float(4)   # y is now an float 4
print(type(x))

"""""
print(.1 + .1 + .1 == .3)

False
""""

# Bit Wise operators


In general, there are two types of errors to look out for

Exceptions
Syntax
An Exception is a problem that occurs when the code is running, but a 'Syntax Error' is a problem detected when Python checks the code before it runs it. For more information, see the Python tutorial page on Errors and Exceptions.




Booleans, Comparison Operators, and Logical Operators
The bool data type holds one of the values True or False, which are often encoded as 1 or 0, respectively.

There are 6 comparison operators that are common to see in order to obtain a bool value:

Comparison Operators
Symbol Use Case	Bool	Operation
5 < 3	False	Less Than
5 > 3	True	Greater Than
3 <= 3	True	Less Than or Equal To
3 >= 5	False	Greater Than or Equal To
3 == 5	False	Equal To
3 != 5	True	Not Equal To
And there are three logical operators you need to be familiar with:

Logical Use	Bool	Operation
5 < 3 and 5 == 5	False	and - Evaluates if all provided statements are True
5 < 3 or 5 == 5	True	or - Evaluates if at least one of many statements is True
not 5 < 3	True	not - Flips the Bool Value
Here is more information on how George Boole changed the world!


if (san_francisco_pop_density > rio_de_janeiro_pop_density):
    print (True)
else:
    print (False)

print(san_francisco_pop_density > rio_de_janeiro_pop_density)


In the video above, at the 1:32 mark, the str is written as follows salesman = '"I think you\'re an encyclopedia salesman'", but the closing string literals should be double quotes " followed by single quotes '.

Strings
Strings in Python are shown as the variable type str. You can define a string with either double quotes " or single quotes '. If the string you are creating actually has one of these two values in it, then you need to be careful to assure your code doesn't give an error.

>>> my_string = 'this is a string!'
>>> my_string2 = "this is also a string!!!"
You can also include a \ in your string to be able to include one of these quotes:

>>> this_string = 'Simon\'s skateboard is in the garage.'
>>> print(this_string)
Simon's skateboard is in the garage.
If we don't use this, notice we get the following error:

>>> this_string = 'Simon's skateboard is in the garage.'
  File "<ipython-input-20-e80562c2a290>", line 1
    this_string = 'Simon's skateboard is in the garage.'
                         ^
SyntaxError: invalid syntax
The color highlighting is also an indication of the error you have in your string in this second case. There are a number of other operations you can use with strings as well. In this video you saw a few:

>>> first_word = 'Hello'
>>> second_word = 'There'
>>> print(first_word + second_word)

HelloThere

>>> print(first_word + ' ' + second_word)

Hello There

>>> print(first_word * 5)

HelloHelloHelloHelloHello

>>> print(len(first_word))

5
Unlike the other data types you have seen so far, you can also index into strings, but you will see more on this soon! For now, here is a small example. Notice Python uses 0 indexing - we will discuss this later in this lesson in detail.

>>> first_word[0]

H

>>> first_word[1]

e
The len() function
len() is a built-in Python function that returns the length of an object, like a string. The length of a string is the number of characters in the string. This will always be an integer.

There is an example above, but here's another one:

print(len("ababa") / len("ab"))
2.5
You know what the data types are for len("ababa") and len("ab"). Notice the data type of their resulting quotient here.
