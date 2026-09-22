#do not allow duplicate,duplicate value will overwrite existing value any type of data
   #can be stored
 # name:vicky--------> name=keys,  vicky=pairs



a={
   "be":"van",
   "he":986,
   "pen":"gear"}
a.update({"he":555})
a.pop(del) #pop is used to delete as
a["colour"]="blue" #using add the new value
print( a.values())
print( a.keys())
print(a.items())
print(a.get("pen")) #it is used to get the what you want