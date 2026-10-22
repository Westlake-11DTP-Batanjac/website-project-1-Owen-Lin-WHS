import math

def circle(r):
    area=r**2 *math.pi
    return area

answer=circle(int(input('number: ')))
print(answer)