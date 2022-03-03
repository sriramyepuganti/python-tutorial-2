#function syntax
def func():
	print("function called")
func()

#function arguments

def argfun(arg1):
	print(arg1)
argfun(10)

#function default arguments

def defargfun(arg1=12):
	print(arg1)
defargfun(10)
defargfun()

#function variable length arguments

def variableargfun(arg1, *varg):
	print(arg1,varg)       #12,(12,3,4,5)
variableargfun(10,12,3,4,5)


#lambda function 

sum = lambda arg1, arg2: arg1 + arg2

# Now you can call sum as a function
print ("Value of total : ", sum( 10, 20 ))
print ("Value of total : ", sum( 20, 20 ))

#import 
import export
export.exported()

#import in another style
from export import exported
exported()

#__name__
print(__name__)

#exceptions
try:
	if(0/0==False):
		print("try")
except ZeroDivisionError:   #NameErro , IndentationError ,IOError , EOFError
	print("catched")
finally:
	print("finally block")