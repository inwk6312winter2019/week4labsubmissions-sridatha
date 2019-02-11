class Time():
	def __init__(self,hours,minute,seconds):
		self.hours = hours
		self.minute = minute
		self.seconds = seconds
	def print_time(self):
		print("{:02}:{:02}:{:02}" .format(self.hours,self.minute,self.seconds))
hours=int(input('Enter hours: '))
minutes=int(input('Enter minutes: '))
seconds=int(input('Enter seconds: '))
time1 = Time(hours,minutes,seconds)
time1.print_time()

