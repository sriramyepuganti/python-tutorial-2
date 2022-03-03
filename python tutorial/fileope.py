#file open operations
from export import exported
fopen = open('text.txt','r')#r,w,a,rb,ab,wb
print(fopen.read())   #read() to read the file
print("file opened succesfully")

fwrite = open('text.txt','a') #write a file
fwrite.write("hello wrold")


