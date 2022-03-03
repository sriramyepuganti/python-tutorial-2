#python single line comment

# python does not allow // single line comment and /**/ multi line comment

"""multi 
line 
comment
"""

#data types in python NUMBER , STRING , TUPLE , LIST, DICTIONARY
#NUMBER -> ing(integers) ex:10 ,float(floating point) ex:0.4 ,complex(2j)
#String -> "hello" 	 , "hello" *2 ->print hello two times , "hello" + " world" string concat , str[2:5] 3rd charcater to 5th

#data casting 

"""
1	
int(x [,base])

Converts x to an integer. The base specifies the base if x is a string.

2	
float(x)

Converts x to a floating-point number.

3	
complex(real [,imag])

Creates a complex number.

4	
str(x)

Converts object x to a string representation.

5	
repr(x)

Converts object x to an expression string.

6	
eval(str)

Evaluates a string and returns an object.

7	
tuple(s)

Converts s to a tuple.

8	
list(s)

Converts s to a list.

9	
set(s)

Converts s to a set.

10	
dict(d)

Creates a dictionary. d must be a sequence of (key,value) tuples.

11	
frozenset(s)

Converts s to a frozen set.

12	
chr(x)

Converts an integer to a character.

13	
unichr(x)

Converts an integer to a Unicode character.

14	
ord(x)

Converts a single character to its integer value.

15	
hex(x)

Converts an integer to a hexadecimal string.

16	
oct(x)

Converts an integer to an octal string.
"""

#python assignment opeartors

# a+=10 -> a = a+10  
# += , -= , *= ,/+ ,**= , //=

##Python Identity Operators   x is y , x is not y 

#python opertor precedence
"""
1	
**

Exponentiation (raise to the power)

2	
~ + -

Complement, unary plus and minus (method names for the last two are +@ and -@)

3	
* / % //

Multiply, divide, modulo and floor division

4	
+ -

Addition and subtraction

5	
>> <<

Right and left bitwise shift

6	
&

Bitwise 'AND'

7	
^ |

Bitwise exclusive `OR' and regular `OR'

8	
<= < > >=

Comparison operators

9	
<> == !=

Equality operators

10	
= %= /= //= -= += *= **=

Assignment operators

11	
is is not

Identity operators

12	
in not in

Membership operators

13	
not or and

Logical operators
"""
 
 #regular expressions
 """
 1	match	This method matches the regex pattern in the string with the optional flag. It returns true if a match is found in the string otherwise it returns false.
2	search	This method returns the match object if there is a match found in the string.
3	findall	It returns a list that contains all the matches of a pattern in the string.
4	split	Returns a list in which the string has been split in each match.
5	sub	Replace one or many matches in the string.
"""