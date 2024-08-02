# func returning two value 
  
def func(int1,int2):
    add  = int1+int2
    multiply = int1*int2
    return add,multiply
print(func(2,3)) # it will give tuple or single value but we want two value fro this we use

add,multiply = func(2,3)
print(add)
print(multiply)