import re

#regex to find IP addresses in the logs
reg1 = re.compile(r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})")

#regex to validate IP Address
reg2 = re.compile(r"((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(\.|$)){4}")

#raw logs
logs = "adj10.33.20.10sdf 10 df 90.30 sdfjk\
sdfj 100.200.300.400 sdf bn 400.300.200 10.20.30.50asdas"

#implementing findall method from regex to find all the occurence in a list
result = reg1.findall(logs)

#iterating over IP addesses list to validate IP
for i in result:
    try:
        if reg2.match(i).group():
            print("Valid IP - {}".format(i))
    except AttributeError:
        print("Not a Valid IP - {}".format(i))


    



