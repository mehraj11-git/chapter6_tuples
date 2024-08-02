# looping in tuples
# tuple with one element
# tuple without parenthesis    
# tuple unpacking    
# list inside tuples
# func that can use with tuples

mixed = (1,2,3,4,5)
for i in mixed:
    print(i)
i = 0
while i <= len(mixed):
        print(i)  
        i +=1  
#  tuple with one element
number = (3)
print(type(mixed)) #this is wrong it is not a one element
print(type(number))
# # we must use the (,) to indicate that it is tuple for ex :
num = (9,)
print(type(num))
# # for this type of number = ('words') use , this string will change into tuple 
worddss = ('words',) 
print(type(worddss)) 

# tuple without parenthesis
bikes = 'yamaha','suzuki','kawasaki' #by defult it will count as a tuple
print(type(bikes))

# tuple unpacking
bikes = 'yamaha','suzuki','kawasaki' # we have gives variable that how many items we have in a variable
bikes1,bikes2,bikes3 = (bikes)       # we cant give less or more 
print(bikes1) 

# list inside tuples
# we can use any mehtods in list as we add list inside tuple.so,we can do changes in list only
friuts = ('mango','banana',['apple','grapes'])
friuts[2].pop()
friuts[2].append('kiwi')
print(friuts)
# func use with tuples
min,max,sum

print(min(mixed))
print(max(mixed))
print(sum(mixed))
