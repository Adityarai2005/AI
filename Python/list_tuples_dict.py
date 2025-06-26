#list and its methods
a=[10,20,30,20]
#a.append(40)#append method adds an element to the end of the list
""" Insert method """
a.insert(0,15)#append at specified position(index,number)
""" remove method """
a.remove(20)#remove method removes the first occurrence of a specified value from the list
""" """ """ pop method """
a.pop(2)#pop method removes the element at the specified index and returns it 
"""Extend method """
num2=[40,50]
a.extend(num2)#extend method adds elements of another list to the end of the list
""" clear delete method """
a.clear()#clear method removes all elements from the list
""" index method """
index=a.index(30)#index method return the index of the first occurence of a specified value
""" count method """
count=a.count(20)#2
""" sort method """
a.sort()#sort method sorts the elements of list in increasing order
""" reverse method """
a.reverse()#reverse method reverses the order of elements

print(a)
""" Tuples and its methods """
a=(10,20,30,20)
"""  count method"""
print(a.count(20))#2
""" index method """
print(a.index(30))#2
""" Tuples are immutable, so we cannot add, remove or modify elements """
""" Dictionaries and its methods """
a={"name":"Aditya","age":20,"city":"Varanasi"}
""" Adding a new key-value pair """
a["country"]="India"#adding a new value pair
#clear method clears all the key-value pairs
""" from keys method """
keys=('a','b','c')
a=dict.fromkeys(keys,0)
print(a['a'])
""" get method """ #a.get('name') returns the value associated with the key 'name'
#items method returns a list of tuples containing key-value pairs
print(a.items())#dict_items([('name', 'Aditya'), ('age', 20), ('city', 'Varanasi'), ('country', 'India')])
""" keys method """
print(a.keys())#dict_keys(['name', 'age', 'city', 'country'])
""" values method """
print(a.values())#dict_values(['Aditya', 20, 'Varanasi', 'India'])
