import random
total = 0

# for num in range(10, -1, -1):
#   print(num)
  
  
x =  random.randint(0,10) 

print(x)

def myFunction(name, age):
  x = 5
  for x in range(1, 10):
    if x == 5:
      print(f"hello {x} {name} {age}")
      
myFunction("David", 30)