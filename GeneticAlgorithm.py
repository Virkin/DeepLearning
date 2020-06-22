import random
from Car import Car

class GeneticAlgorithm :
	pCo = 0.8
	pM = 0.2

	nbParents = 2

	def __init__(self, pop) :
		self.pop = pop
		self.popSize = len(pop)
		self.networkNbLayer = len(pop[next(iter(pop))][0])

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
				newIndiv = self.crossover()
				if m <= self.pM :
					newIndiv = self.mutation(newIndiv)
			else :
				newIndiv = Car()
				
			
	def selection(self) :
		bestParents = []

		for indiv in self.pop :
			if len(bestParents) < self.nbParents :
				bestParents.append(indiv)
			elif indiv.score > bestParents[-1].score :
				for i in range(nbParents) :
					if indiv.score > bestParents[i].score :
						bestParents.insert(i,indiv)
						bestParents.pop()
						break
		return bestParents

	def crossover(self, parents) :

		newIndiv = Car()

		weights = newIndiv.getNetworkLinkWeights()

		for i in range(self.networkNbLayer) :
			choosePar = random.randrange(len(parents))
			parWeights = parents[choosePar].getNetworkLinkWeights()
			weights[i] = parWeights[i]

		newIndiv.setNetworkLinkWeights(weights)

		return newIndiv

	def mutation(self, indiv) :
		
		pass

		