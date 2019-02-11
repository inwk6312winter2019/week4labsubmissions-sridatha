class Time():
	def __init__(self,hours,minute,seconds):
		self.hours = hours
		self.minute = minute
		self.seconds = seconds
	def print_time(self):
		print("{:02}:{:02}:{:02}" .format(self.hours,self.minute,self.seconds))


	def is_after(self,t2):
		return ((self.hours)*3600 + (self.minute)*60 + self.seconds < (t2.hours)*3600 + (t2.minute)*60 + t2.seconds)

time1 =  Time(10,30,29)
time2 =  Time(40,30,19)

print(time1.is_after(time2))

