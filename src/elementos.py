#elementos.py
class Ball():
	def __init__(self):
		self.limiarizacao = Limiarization()
		print("oi")
		
class Limiarization():
	def __init__(self) -> None:
		self.lim_min = [255,255,255]
		self.lim_max = [0,0,0]

	def update(self, hue, saturation, value) -> None:
		if hue > self.lim_max[0]: self.lim_max[0] = hue
		if hue<=self.lim_min[0]: self.lim_min[0] = hue-1
		if saturation>self.lim_max[1]: self.lim_max[1] = saturation
		if saturation<=self.lim_min[1]: self.lim_min[1] = saturation-1
		if value>self.lim_max[2]: self.lim_max[2] = value
		if value<=self.lim_min[2]: self.lim_min[2] = value-1

	def update2(self, hue, saturation, value) -> None:
		self.lim_max[0] = hue
		self.lim_min[0] = hue
		self.lim_max[1] = saturation+10
		self.lim_min[1] = saturation-10
		self.lim_max[2] = value
		self.lim_min[2] = value