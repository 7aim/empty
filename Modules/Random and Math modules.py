import random
import math

#ramdom

print(random.randint(1,5))

print(random.choice([1,4,5,3]))

print(random.choices([1,4,5,3],k=2)) #k number, repeats

print(random.sample([1,4,5,3],k=2)) #k number, no repeats

list = [1,4,5,3]
random.shuffle(list) #shuffle the list.You must provide the list beforehand (it does not return a value on its own)
print(list)

#math

print(math.ceil(5.5)) #top value
print(math.floor(5.5)) #lower value
print(math.factorial(5)) #calculate fac
