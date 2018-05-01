class First(object):
    def __init__(self):
        super(First, self).__init__()
        print("first")

class Second(object):
    def __init__(self):
        super(Second, self).__init__()
        print("second")

class Third(First, Second):
    def __init__(self):
        super(Third, self).__init__()
        print("third")


Third()

#According to MRO __init__ of Third is called first.
#Next, according to the MRO, inside the __init__ method super(Third,
#self).__init__() resolves to the __init__ method of First, which gets called.
#Inside __init__ of First super(First, self).__init__() calls the __init__ of Second, because that is what the MRO dictates!
#Inside __init__ of Second super(Second, self).__init__() calls the __init__ of object, which amounts to nothing. After that "second" is printed.
#After super(First, self).__init__() completed, "first" is printed.
#After super(Third, self).__init__() completed, "that's it" is printed.

## More explanantion ##

#I think Step 3 needs more explanation: If Third did not inherit from Second, then super(First, self).__init__ would call object.__init__ and after returning, "first" would be printed. But because Third inherits from both First and Second, rather than calling object.__init__ after First.__init__ the MRO dictates that only the final call to object.__init__ is preserved, and the print statements in First and Second are not reached until object.__init__ returns. Since Second was the last to call object.__init__, it returns inside Second before returning in First
