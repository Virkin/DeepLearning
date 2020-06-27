from LogicCar import LogicCar
from GraphicCar import GraphicCar

import math

from PyQt5.QtGui import QColor

class Car :
	def __init__(self, baseWidth, baseHeight, canvas, x=400, y=300) :
		self.logic = LogicCar()
		self.graph = GraphicCar(baseWidth, baseHeight, canvas, x=x, y=y)

	def run(self) :
		if not self.graph.collides(QColor('black')):
			self.logic.predictNextConf(self.graph.getSensor())
			
			aRad = math.radians(self.graph.graphic_a+90)+self.logic.turn

			self.graph.graphic_x += round(math.cos(aRad)*self.logic.speed).astype(int)
			self.graph.graphic_y -= round(math.sin(aRad)*self.logic.speed).astype(int)

			if self.graph.graphic_x < 0 :
				self.graph.graphic_x = 0

			if self.graph.graphic_y < 0 :
				self.graph.graphic_y = 0

			self.graph.graphic_a = math.degrees(aRad - math.pi/2)

			print("id:{} / x : {}/y : {}\n".format(self.logic.id, self.graph.graphic_x, self.graph.graphic_y))
		else :
			pass

