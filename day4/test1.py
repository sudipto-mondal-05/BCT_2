import numpy as n

arr=n.array([10,20,30,40,50,60,70,80,90,100])
indices=n.array([1,3,5])
print("integer array indexing:",arr[indices])
cond=arr>0
print("\nelements greater than 0:\n",arr[cond])

x=n.array([1,2,3])
y=n.array([1,2,7])
a=x+y
print("add:",a)
b=x*y
print("multi:",b)
c=x-y
print("sub:",c)
d=x/y
print("div:",d)

arr=n.array([1,2,3,-4,0])
result=n.absolute(arr)
print("absolute val:",result)

a1 = n.array([1,2,3])
print("Sin val: ", n.sin(a1))
print("Exp val: ", n.exp(a1))
print("Sqrt val: ", n.sqrt(a1))
