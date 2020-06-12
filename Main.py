from Car import Car

nbCar = 20

if __name__ == "__main__":
	
	carList = []

	for i in range(nbCar) :
		carList.append(Car())

	firstCar = carList[0]

	firstCar.updateSensor()

	print(firstCar.getSensorValue())

	firstCar.predictNextConf()

	print("Init speed : {} / Init turn : {}".format(firstCar.speed, firstCar.turn))

	firstCar.updateSensor()

	firstCar.predictNextConf()

	print(firstCar.getSensorValue())

	print("Next speed : {} / Next turn : {}".format(firstCar.speed, firstCar.turn))
