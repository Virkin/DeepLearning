from NeuralNetwork import NeuralNetwork

import random

class Car :

	speed = 0
	turn = 0
	sensor = [0,0,0,0,0]

	score = 0

	def __init__(self) :
		self.ann = NeuralNetwork()

	def updateSensor(self) :
		#Random update for test

		for i in range(len(self.sensor)) :
			self.sensor[i] = random.uniform(0,1)

	def getSensorValue(self) :
		return self.sensor

	def predictNextConf(self) :
		output = self.ann.getPrediction(self.sensor)
		self.speed = output[0][0]
		self.turn = output[0][1]

	def getScore(self) :
		return self.score