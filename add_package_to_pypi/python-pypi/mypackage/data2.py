d1 = {'name':['deep','sonu','abhi']}
d2 = {'name':['abhi','sonu','deep']}


def compare_dict_column(d1,d2):
    flag = 0
    try:
        if d2.has_key(d1.keys()[0]):
            print "key matched"
        else:
            print "Key not matched"
            return False 

        for val in d1.values()[0]:
            if val in d2.values()[0]:
                print "value matched"
            else:
                print "Value not match"
                return False
    except (KeyError,ValueError):
        raise RuntimeError("Error in column values")
    

    if flag == 0:
        return True
    else:
        return False

			
st = compare_dict_column(d1,d2)
print "status -- %s"%st
            
			    
