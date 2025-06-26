str1="hello"
str2="world"
#concatenation
print(str1+" "+str2)
#repetition
print(str1*2)
#len
print(len(str1))
#upper and lower
print(str1.upper())
#capitalize
print(str1.capitalize())#Hello
""" title is capitalize to every word of string """
"""  strip  is used to remove leading and trailing white spaces"""
#replace()
a="hello !world"
print(a.replace("world","duniya"))#hello duniya
#split()
""" this function splits the string into an array with words """
print(a.split("!"))#['hello ', 'world']
print(a.split())#['hello', '!world']
#join()
""" this function joins the elements of an array into a string """
b=["hello","world"]
print(" ".join(b))#hello world space is added between words
#find()
""" this function returns the index of the first occurrence of a substring """
print(a.find("world"))#7
""" format method """
name="Aditya"
age=20
msg="My name is {} and I am {} years old".format(name,age)
#formatting with f-string
print(f"My name is {name} and I am {age} years old")
""" Translate method """
inlang="abcde"
outlang="12345"
translang=str.maketrans(inlang,outlang)
print("azvmeighou".translate(translang))