class Count():
	def __init__(self,list):
		self.list = list
		x = []
		for j in self.list:
			if self.list.count(j) == 1:
				x.append(j)
		for i in self.list:
			if self.list.count(i) > 1:
				self.list.remove(i)
		for k in x:
			for l in self.list:
				if k == l:
					self.list.remove(k)
		print(self.list)
#a = [1,1,2,3,4,4,7,7,9,0,0]
#Count(a)

