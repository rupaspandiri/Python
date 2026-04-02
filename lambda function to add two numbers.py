add=lambda x,y:x+y
print(add(4,6))


square=lambda x:x**2
print(square(5))


cube=lambda x:x**3
print(cube(5))



check=lambda x:x%2==0
print(check(3))

nums=[1,2,3,4,5,6]
print(list(map(lambda x:x+5,nums)))


list1=[1,2,3,4,5]
list2=[4,5,2,5,6]
print(list(map(lambda x,y:x*y,list1,list2)))


list1=[1,2,3,4,5,6]
print(list(filter(lambda x:x%2==0,list1)))


from functools import reduce
l=[1,2,3,4,5,6]
print(reduce(lambda x,y:x+y,l))


check=lambda x:x%2==1
print(check(2))



from functools import reduce
str1="PANDIRI"
str2=" RUPAS"  
print(str(reduce(lambda x,y:x+y,str2,str1)))
