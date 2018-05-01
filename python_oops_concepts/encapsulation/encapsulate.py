class encapsulate():
    def __init__(self, pub, prot, pri):
        self.pub = pub #public
        self._prot = prot #protected
        self.__pri = pri  #private


a = encapsulate(10,20,30)

print a.pub
print a._prot
#print a.__pri   "accessing private variables directly, This will give error"

"""put a dir on a you will see that pub and _prot are in scope of a but _encapsulate__pri is also there so you can 
access the pri by this"""

print a._encapsulate__pri
