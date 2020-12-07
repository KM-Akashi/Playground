import numpy as np
import random


class Population(object):

    def __init__(self, fitness_funcation, domain, init_number):
        self.fitness_funcation = fitness_funcation
        self.domain = domain
        low_len = domain[0].bit_length() + 1
        high_len = domain[1].bit_length() + 1
        self.size = max(low_len, high_len)
        self.init_number = init_number
        self.population = np.random.randint(
            2, size=(init_number, self.size)).astype(np.bool)

    def decode(self, individual):
        res = 0
        for bit in individual[1:]:
            if bit:
                res = (res << 1) + 1
            else:
                res = (res << 1)
        if individual[0]:
            res = - res
        if res < self.domain[0]:
            res = self.domain[0]
        elif res > self.domain[1]:
            res = self.domain[1]
        return res

    def encode(self, individual):
        res = []
        if individual < self.domain[0]:
            individual = self.domain[0]
        elif individual > self.domain[1]:
            individual = self.domain[1]
        bits = format(individual, 'b')
        if individual < 0:
            res.append(True)
            for bit in bits[1:]:
                if bit is '1':
                    res.append(True)
                else:
                    res.append(False)
        else:
            res.append(False)
            for bit in bits:
                if bit is '1':
                    res.append(True)
                else:
                    res.append(False)
        return res

    def fitness(self, individual):
        return self.fitness_funcation(individual)

    def mutation(self):
        index = random.randint(0, self.population.shape[0]-1)
        position = random.randint(0, self.population.shape[1]-1)
        self.population[index, position] = not self.population[index, position]

    def crossover(self):
        while self.population.shape[0] < self.init_number:
            x = random.randint(0, self.population.shape[0]-1)
            y = random.randint(0, self.population.shape[0]-1)
            mid = int(self.size / 2)
            new_dna = np.append(
                self.population[x, mid:], self.population[y, :mid])
            self.population = np.vstack((self.population, new_dna))

    def select(self, epoch):
        for _ in range(epoch):
            score_list = []
            for index in range(self.init_number):
                score = self.fitness(self.decode(self.population[index]))
                score_list.append((index, score))
            score_list.sort(key=lambda n: -n[1])
            delete_list = []
            mid = int(len(score_list)/2)
            for score_dna in score_list[mid:]:
                delete_list.append(score_dna[0])
            self.population = np.delete(self.population, delete_list, axis=0)
            self.crossover()
            self.mutation()
            self.mutation()
            self.mutation()

        for index in range(self.init_number):
            score = self.fitness(self.decode(self.population[index]))
            score_list.append((index, score))
        score_list.sort(key=lambda n: -n[1])
        print(score_list)


if __name__ == "__main__":
    def f(x):
        return -(x**2) + 10*np.cos(2*np.pi*x) + 30
    p = Population(f, (-5, 5), 5)
    p.select(10000)
