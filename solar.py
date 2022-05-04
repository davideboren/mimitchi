import numpy
import math
class Solar():
	def __init__(self):

		#Length of full day in minutes
		self.day_length = 240
		self.frame_rate = 60
		self.frame_counter = 0
		self.minute = 0

		self.tint_key = [
			(255,255,255),
			(255,255,255),
			(255,150,55),
			(60,60,170)
		]

		self.tint = (255,255,255)

		self.shadow_w = 80
		self.shadow_h = 16
		self.shadow_dx = -16
		self.shadow_dy = 48

		self.update_shadow_values()

	def update(self):
		if self.frame_counter >= self.frame_rate * 60:
		#if self.frame_counter >= 8:

			if self.minute >= self.day_length - 1:
				self.minute = 0

			self.frame_counter = 0

			self.minute += 1
			print(self.minute)

			self.update_tint() 
			self.update_shadow_values()

		self.frame_counter += 1

	def update_tint(self):
		pos = float(self.minute / self.day_length) * len(self.tint_key)
		if int(pos) == 0:
			pct = pos
		else:
			pct = pos % int(pos)
		diff = numpy.subtract(self.tint_key[(int(pos)+1) % len(self.tint_key)], self.tint_key[int(pos)])
		to_add = numpy.multiply(diff,pct)
		adj_tint = numpy.add(self.tint_key[int(pos)],to_add)
		self.tint = tuple( [int(adj_tint[0]), int(adj_tint[1]), int(adj_tint[2])] )

	def get_tint(self):
		return self.tint

	def update_shadow_values(self):
		self.shadow_w = 32 * math.cos(((self.minute / (self.day_length/2)) * 2 * math.pi)) + 96
		self.shadow_dx = (self.shadow_w/8) * -math.cos(((self.minute / (self.day_length/2)) *  math.pi)) - (self.shadow_w/4)

