from math import sqrt
class Point():
	"""anything"""
point=Point()
point.x1=int(input('enter a point x1: '))
point.y1=int(input('Enter a point y1: '))
point.x2=int(input('Enter a point x2: '))
point.y2=int(input('Enter a point y2: '))
def distance_between_points(x1,y1,x2,y2):
	return(sqrt((x2-x1)**2+(y2-y1)**2))

print(distance_between_points(point.x1,point.y1,point.x2,point.y2))


