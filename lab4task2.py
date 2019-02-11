from math import sqrt
class Point():
	"""anything"""
class Rectangle():
	def __init__(self,width, height,corner):
		self.width=width
		self.height=height
		self.corner=Point()



class move_rectangle():
	def __init__(self,dx,dy)

rec=Rectangle(100,200,Point())
rec.width=int(input('Enter width of the Rectangle: '))
rec.height=int(input('Enter height of the Rectangle: '))
rec.corner.x1=int(input('enter a point x1: '))
rec.corner.y1=int(input('Enter a point y1: '))
rec.corner.x2=int(input('Enter a point x2: '))
rec.corner.y2=int(input('Enter a point y2: '))
def find_center(x1,y1,x2,y2):
	return ((x2+x1)//2,(y2+y1)//2)

print(find_center(rec.corner.x1,rec.corner.y1,rec.corner.x2,rec.corner.y2))


