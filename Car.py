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
			#print(self.graph.getSensor())

			val = self.logic.predictNextConf(self.graph.getSensor())

			if val < 0.25 :
				retVal = self.graph.moveLeft()
			elif val >= 0.25 and val < 0.5 :
				retVal = self.graph.moveUp()
			elif val >= 0.5 and val < 0.75:
				retVal = self.graph.moveRight()
			else :
				retVal = self.graph.moveDown()

			oldScore = self.logic.score

			self.updateScore()

			return retVal
			"""
			aRad = math.radians(self.graph.graphic_a+90)+self.logic.turn

			self.graph.graphic_x += round(math.cos(aRad)*self.logic.speed).astype(int)
			self.graph.graphic_y -= round(math.sin(aRad)*self.logic.speed).astype(int)

			if self.graph.graphic_x < 0 :
				self.graph.graphic_x = 0

			if self.graph.graphic_y < 0 :
				self.graph.graphic_y = 0

			self.graph.graphic_a = math.degrees(aRad - math.pi/2)

			print("id:{} / x : {}/y : {}\n".format(self.logic.id, self.graph.graphic_x, self.graph.graphic_y))"""
		else :
			return False

	def updateScore(self) :
		self.logic.score += abs(self.graph.graphic_lastX - self.graph.graphic_x) + abs(self.graph.graphic_lastY - self.graph.graphic_y)

