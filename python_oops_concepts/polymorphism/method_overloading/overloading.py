########################################################################
#
# method overloading based on parameters
# In this example sayHello method is called with and without parameters
#
########################################################################

class Human():
 
    def sayHello(self, name=None):
 
        if name is not None:
            print 'Hello ' + name
        else:
            print 'Hello '
 
# Create instance
obj = Human()
 
# Call the method
obj.sayHello()
 
# Call the method with a parameter
obj.sayHello('Guido')
