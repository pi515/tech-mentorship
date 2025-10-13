# Class definition
class myClass:
  # Class variables
  myClassVar = 'Class Variable'

  # Constructor
  def __init__(self, arg1):
    # Instance variables
    self.myInstanceVar = arg1

  # Instance method
  def myMethod(self):
    print(self.myClassVar + ' from instance method')
    print(self.myInstanceVar + ' from instance method')

    
# Program Start

# Calling constructor
obj = myClass('Instance Variable')

# Printing class and instance variables
print(obj.myClassVar)
print(obj.myInstanceVar)

# Calling instance method
obj.myMethod()