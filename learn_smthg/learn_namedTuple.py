from collections import namedtuple 

point = namedtuple('Point', 'x,y')

p1= point(1,2)
p2= point(3,4) 

dot_prod= (p1.x* p2.x) + (p1.y * p2.y)  
print(dot_prod) # answer = 11
print('='* 20)
print()

car = namedtuple('Car', 'Price milieage colour Class') 
xyz = car(Price=1000, milieage=42, colour='blue', Class='s')  
print(xyz)
print()
# lis = ['Price', 'milieage', 'colour', 'Class']
lis = ['Price milieage colour Class']
# for i in lis:
#     print(xyz.i) 

print(xyz.Class)
print(xyz.colour)
print(xyz.Price)
print('='*40)
print()  


