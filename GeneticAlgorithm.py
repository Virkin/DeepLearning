import random
from Car import Car

class GeneticAlgorithm :
	pCo = 0.7
	pM = 1

	nbParents = 2

	def __init__(self, pop) :
		self.pop = pop
		self.popSize = len(pop)
		self.networkNbLayer = len(pop[0].logic.getNetworkLinkWeights())

		print(self.networkNbLayer)


	def run(self):
		newPop = []

		parents = self.selection()

		for par in parents :
			newPop.append(par)

		for i in range(len(self.pop)-self.nbParents) :

			co = random.uniform(0,1)
			m = random.uniform(0,1)

			if co <= self.pCo :
				newIndiv = self.crossover(parents)
				if m <= self.pM :
					newIndiv = self.mutation(newIndiv)
			else :
				newIndiv = self.createNewIndiv()

			newPop.append(newIndiv)

		return newPop

				
			
	def selection(self) :
		bestParents = []

		for indiv in self.pop :

			if len(bestParents) < self.nbParents :
				bestParents.append(indiv)
			elif indiv.logic.score > bestParents[-1].logic.score :
				for i in range(self.nbParents) :
					if indiv.logic.score > bestParents[i].logic.score :
						bestParents.insert(i,indiv)
						bestParents.pop()
						break

		for par in bestParents :
			par.logic.score = 0
			par.graph.graphic_x = 75
			par.graph.graphic_y = 60
			par.graph.graphic_a = 180
			par.graph.saveLast()
		return bestParents

	def crossover(self, parents) :

		newIndiv = self.createNewIndiv()

		weights = newIndiv.logic.getNetworkLinkWeights()

		for i in range(self.networkNbLayer) :
			choosePar = random.randrange(len(parents))
			parWeights = parents[choosePar].logic.getNetworkLinkWeights()
			weights[i] = parWeights[i]

		newIndiv.logic.setNetworkLinkWeights(weights)

		return newIndiv

	def mutation(self, indiv) :

		nbMutation = 20

		weights = indiv.logic.getNetworkLinkWeights()

		for i in range(nbMutation) :			

			layer = random.randrange(self.networkNbLayer)

			link = random.randrange(len(weights[layer]))

			offset = random.randint(1,2)

			weights[layer][link] += 0.2*pow(-1,offset)

		indiv.logic.setNetworkLinkWeights(weights)

		return indiv

	def createNewIndiv(self) :

		newIndiv = Car(self.pop[0].graph.graphic_w/5, self.pop[0].graph.graphic_h/4, self.pop[0].graph.canvas, 75, 60)
		newIndiv.graph.graphic_a = 180

		return newIndiv

		