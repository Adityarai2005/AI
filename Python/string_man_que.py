""" reverse a string"""
s="hello world"
t="hello world"
a=list(s)
a.reverse()
ans="".join(a)
ans1=s[::-1]
""" check if a string is pallindrome or not """
print(s==t)
""" Count Vowels in a string"""
v=['a','e','i','o','u']
count=0
for i in s:
    if i in v:
        count+=1
print(count)