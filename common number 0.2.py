class Count():
	def __init__(self,list):
		self.list = list
	def common_number(self):
		x = []
		for j in self.list:
			if self.list.count(j) >= 2:				
				x.append(j)
		for i in x:
			if x.count(i) > 1:
				x.remove(i)
			for k in x:
				if x.count(k) !=1 :
					x.remove(k)
		return x
a = [1,1,2,3,4,4,6,7,7,8,8,8,0,0,0,0,0,0]
number = Count(a).common_number()
print(number)