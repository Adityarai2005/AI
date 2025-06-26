#list comprehension
""" create a list of  numbers 0 to 9 """
x=[x for x in range(10)]
""" filter even number """
x=[x for x in range(10) if x%2==0]
""" keep only perfect squares """
x=[x**2 for x in range(10) if x**2 <10 ]
#Dictionary comprehension
""" create a dictionary with values as square of the key """
a={x:x**2 for x in range(10)}
""" filter dictionary where items where the value is even """
even_dict={k:v for k,v in a.items() if v%2==0 }
#tuples comprehension
""" create a list of tuples from two lists """
names=['Alice','Bob','John']
scores=[85,90,95]
y=[(name,score)for name,score in zip(names,scores)]
#set comprehension
phrase="hello world"

vowels=set(word for word in phrase if word in 'aeiou')
print(vowels)
""" get the length of each string in list """
li=['word','are','for','test']
a=[len(z) for z in li]
""" transposing a 2D matrix """
matrix=[[1,2,3],[4,5,6],[7,8,9]]
transpose=[[row[i] for row in matrix]for i in range(len(matrix[0]))]
print(transpose)