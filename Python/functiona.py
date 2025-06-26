#build in functions
""" print(),input(),len() """
#user defined function
def add(n1,n2):#parameters
   return n1+n2
print(add(1,2))#arguements
""" default parameters """
def abc(name,age,country="india"):
   print(f"{name},{age},{country}")
abc("aditya",20,)
abc("aditya",20,"japan")
abc(name="vaibhav",age=17,country="indonessia")#key word arguement
