from LogicCar import LogicCar
from GraphicCar import GraphicCar

class Car :
	def __init__(self, baseWidth, baseHeight, canvas, x=400, y=300) :
		self.logic = LogicCar()
		self.graph = GraphicCar(baseWidth, baseHeight, canvas, x=x, y=y)

