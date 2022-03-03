class Myclass:
    name = ""
    def __init__(self):
        self.name ="hello world"
    def fun(self):
        print(self.name)
obj = Myclass()
#obj.id
obj.fun()
print(obj.__dict__)
print(obj.__doc__)
print(__name__)
print(obj.__module__)
#print(__bases__)


#inheritance

class Parent:        # define parent class
   parentAttr = 100
   def __init__(self):
      print ("Calling parent constructor")

   def parentMethod(self):
      print ('Calling parent method')

   def setAttr(self, attr):
      Parent.parentAttr = attr

   def getAttr(self):
      print ("Parent attribute :", Parent.parentAttr)

class Child(Parent): # define child class
   def __init__(self):
      super().__init__()
      print ("Calling child constructor")
#print(self.parentMethod())

   def childMethod(self):
      print ('Calling child method')

c = Child()          # instance of child
c.childMethod()      # child calls its method
c.parentMethod()     # calls parent's method
c.setAttr(200)       # again call parent's method
c.getAttr()          # again call parent's method

#data hiding 
class JustCounter:
   __secretCount = 0
  
   def count(self):
      self.__secretCount += 1
      print (self.__secretCount)

counter = JustCounter()
counter.count()
counter.count()
print (counter.__secretCount)  #it is not allow to display data