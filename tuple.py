#tuple
  #allow d((uplicate, any data type stored, cannot modify,
#use count(),indexing


a=(1,3,5,6,8,3,3,3)
b=(2,4,7,0)
c=list(b)     #but we can  do casting
d=type(c)
print("the count the duplicate value" ,a.count(3))
print("to indexing the value to enter:",a[4])
print(c)
print(d)