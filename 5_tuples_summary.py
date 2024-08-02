# tuples are ordered collection of items
# tuples store any type of data 
# tuples are immutable 
# we use parenthesis for tuple()
# we cannot make changes in tuples but we can do changes in list which is present inside tuples
#we use this method if we dont want to change anything for ex we cannot changes days monday tuesday ect..
 

mixed = (1,2,3,4,5,'six')
# no append ,no pop , no insert,no remove,no extend , no del
# only 
# index,count,slicing
# functions
# len(),min(),max(),sum()

mixed2 = (1,2,5,[2,3,5,]) #we should avoid making list inside tuples bcz it makes trouble while we make big progamme
mixed2[3].pop()
print(mixed2)