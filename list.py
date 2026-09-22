#LIST           #allow depilicate
                #any data type can stored
                #modify,add,remove
                #insert(),append(),extend(),pop()

a=[1,9,0,8,7] 
b=[11,33,55,66] 
a.append(7)
a.insert(3,100)
a.update([2])
a.pop(4) #if we pop(remove) the value by intex is use pop, not remove word
a[2]=3 # it as using to exchanging the value by using index
a.remove(1)
a.extend(b)


print(a)