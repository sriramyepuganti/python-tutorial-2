
#data assigning types

direct = 1  
#multiplt assignment
oneway1 = oneway2 = oneway3 = 5
secondway1 , secondway2 , secondway3 = 1,2,4 
print(oneway2)
print(secondway2)

#data types test in python

integer = 32
floating = 45.45
longnum = 10278463777483789743988943
imaginary = 2j
string = "hiiiii"
print(type(integer))  #integer is <class 'int' > 
print(type(floating))  #floating is <class 'float' > 
print(type(imaginary)) #imaginary is <class 'complex'>
print(type(string))  #string is <class 'str'>

#data type casting

casttest = 4
print(oct(casttest))

#stdio 

print("hello world") #standrad output in python
a = input()  #it retur string value
print("input value " + a) #standard input in python

#arthmetic operations 
opearnd1 = 30
opearnd2 = 12

print("opearnd1 + opearnd2="+ str(opearnd1+opearnd2) )
print("opearnd1 - opearnd2="+ str(opearnd1-opearnd2) )
print("opearnd1 * opearnd2="+ str(opearnd1*opearnd2) )
print("opearnd1 / opearnd2="+ str(opearnd1/opearnd2) )#it gives 15/2=7.5
print("opearnd1 % opearnd2="+ str(opearnd1%opearnd2) )
print("opearnd1 // opearnd2="+ str(opearnd1//opearnd2) )#it gives 15//2=7
print("opearnd1 ** opearnd2="+ str(opearnd1**opearnd2) )#power

#comparsion opeartor 

comp1 = 12
comp2 = 13

print("a==b="+str(comp1==comp2))  #False
print("a!=b="+str(comp1!=comp2))  #True
print("a>b="+str(comp1>comp2))
print("a<b="+str(comp1<comp2))
#print("a<>b"+str(comp1<>comp2))

#python bitwise operators

bit1 = 10 
bit2 = 20

print("bit1 | bit2 =" + str(bit1 | bit2))
print("bit1 & bit2 =" + str(bit1 & bit2))
print("bit1 ^ bit2 =" + str(bit1 ^ bit2))
print(" ~ bit2 =" + str( ~ bit2))

#python logical opertors

log1 = True
log2 = False
print("log1 and log2 =" + str(log1 and log2))
print("log1 or log2 =" + str(log1 or log2))
print("not(log1 and log2) =" + str(not(log1 and log2)))

#Python Membership Operators
array = [1,23,4]
print("23 in array=" + str(23 in array))
print("23 not in array=" + str(23 not in array) )

#####decision making

#if else
ifelsetest = 35
if(ifelsetest==34):
	print("ifcondition is excuted")
else:
	print("else is excuted")

#elseif test

elseiftest = 45
if(elseiftest <20):
	print("value is less than 20")
elif(elseiftest <50):
	print("value is less than 50 and greated than 20")
else:
	print("value is greater than 50")

#single statement in if then 

singleif = 34
if(singleif==34): print("single if is excuted")

######loops 

#for loop
forarray = [1,2,3,4,5,6,7,8]
for x in forarray:
	print(x)
for x in range(10,20):
	print(x)
stringfor = "hello world"
for x in stringfor:
	print(x)
#while loop
whilecount = 0
while(whilecount < 10):
	print(whilecount)
	whilecount+=1
####control statements 
#break ,continue , pass

#lists ->we can update and delete the element in list
lists = [1,2,3,4,5]
del lists[0]
print(lists)
 #tuples -> we can't change 
tupless = (1,2,3,4,5)
#del tupless[0]  update and delete is not possible
print(tupless)

#dictinary ->del dict ->delete entire dict and dict.clear() removes particulst dict
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'} #it does not print duplicate keys

print(dict)

#sets
sets = {"sri","ram","sai"} #it does not print duplicate

print(sets) #print sets in random order

#date and time
import time;      # This is required to include time module.

ticks = time.time()
print ("Number of ticks since 12:00am, January 1, 1970:", ticks)

#calender
import calendar

cal = calendar.month(2016, 2)
print ("Here is the calendar:")
print (cal)

#with keyword

file = open('file_path', 'w') #with out with
try: 
	file.write('hello world') 
finally: 
    file.close() 
with open('file_path', 'w') as file: #with keyword,it handles error and closeing of file
    file.write('hello world !')
#with for user defined objects
class MessageWriter(object): 
	def __init__(self, file_name): 
		self.file_name = file_name  
	def __enter__(self): 
		self.file = open(self.file_name,'a')
		return self.file 
	def __exit__(self): 
		self.file.close()   
# using with statement with MessageWriter   
with MessageWriter('ext.txt') as xfile: 
	xfile.write('hello world') 
