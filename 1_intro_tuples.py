# tuples = this is also use for to store data but this method use paranthysis ( )
# tuples are immutable means unchangeable 
# we can storee  any type of data 
# ex : 
# example = ('one', 'word', 'three' ,10 , 12)
#  we cannot use 
# append
# insert 
# pop 
# remove methods bcz tuples are immutable

# we use this methods when we donot want to change anything 
# ex : days = ('monday','tuesday')
# tuples are faster than list 
# we can use 
# count
# len function
# index 
# slicing methods 

example = ('one', 'word', 'three' ,10 , 12)
# print(example.count('word')) # count
# print(len(example)) # len func
# print(example[3])   # index
# print(example[:2])  # slicing method

# we cannot change data 
example[0] = 1
print(example)
