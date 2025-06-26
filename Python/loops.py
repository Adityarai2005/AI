
i=1
for i in range(11):
 print(i)
for i in range(1,11,2):
 print(i)
 # for loop in tuple
tup=(1,2,3,4)
for i in tup:
  print(i)
# for loop in dictionary
dict1={"name":"Aditya","age":20,"city":"Varanasi"}
for i in dict1:
    print(i)  #print only keys
#another way to print keys and values
for key,value in dict1.items():
   print(f"{key}:{value}")
   """ while loops """# mostly used in automation for infinte loops
j=0
while j<5:
   print(j)
   j+=1
""" while with tuples """
a=('a','b','c')
i=0
while i <len(a):
   print(a[i])
   i+=1
   #simlarly with dictionarires use .items()
   