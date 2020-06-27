from Car import Car
from GeneticAlgorithm import GeneticAlgorithm as Ga
nbCar = 20

def runSimu(carList) :
	return carList



if __name__ == "__main__":
	
	carList = []
	nbGénération = 1

	for i in range(nbCar) :
			carList.append(Car(i))

	#while True :

	carList = runSimu(carList)

	ga = Ga(transformsCarsToPop(carList))

	#carList = ga.run()

	nbGénération += 1

	


	firstCar = carList[0]

	firstCar.getNetworkLinkWeights()

	"""firstCar.updateSensor()

	print(firstCar.getSensorValue())

	firstCar.predictNextConf()

	print("Init speed : {} / Init turn : {}".format(firstCar.speed, firstCar.turn))

	firstCar.updateSensor()

	firstCar.predictNextConf()

	print(firstCar.getSensorValue())

	print("Next speed : {} / Next turn : {}".format(firstCar.speed, firstCar.turn))"""
