#Program = Calculate area of circle
#input = radius
#output is area
import math

#Data types
#input -> int or float ->float
#outpot -> float as it involves pi

#Core logic -> formula -> pi*r*r

radius = float(input("Enter the radius"))
#radius = float(radius)
print(math.pi)
area = math.pi*(radius**2)
area2=math.pi*(math.pow(radius, 2))
print(area)
print(area2)



