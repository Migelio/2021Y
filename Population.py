import numpy as np
import random as rn
class Population:
    def __init__(self, N):
        self.N = N
        file = open(r'C:\myProgram\py\Kolganov\input1.txt', 'r')
        data = file.readlines()
        for i in range(len(data)):
            data[i] = data[i].split(' ')
            while(True):
                try:
                    data[i].remove('')
                except ValueError:
                    break
        self.mes = []
        for i in range(len(data)):
            self.mes.append([float(data[i][0])/1000, float(data[i][1])/1000, float(data[i][2])/1000])
        self.mes = np.array(self.mes)
        self.population = np.zeros([N, 8])
        
        for i in range(self.N):
            self.population[i][0] = rn.random() *2 - 1
            self.population[i][1] = rn.random() *2 - 1
            self.population[i][2] = rn.random() *2 - 1
            self.population[i][3] = rn.random() *6 - 3
            self.population[i][4] = rn.random() *6 - 3
            self.population[i][5] = rn.random() *6 - 3
    def square_sum(self, mes, example):
        dH1 = example[0]
        dH2 = example[1]
        dH3 = example[2]
        dK1 = example[3]
        dK2 = example[4]
        dK3 = example[5]
        # Suma = 0
        # for i in mes:
        #     Suma += (1 - (((i[0] - dH1)/(1 + dK1))**2 + ((i[1] - dH2)/(1 + dK2))**2 + ((i[2] - dH3)/(1 + dK3))**2))**2
        # return Suma
        return np.sum((1 - (((mes[:, 0] - dH1)/(1 + dK1))**2 + ((mes[:, 1] - dH2)/(1 + dK2))**2 + ((mes[:, 2] - dH3)/(1 + dK3))**2))**2)
    def calc_fitness(self):
        for i in range(self.N):
            self.population[i][6] = Population.square_sum(self.mes, self.population[i])
        AntiSuma = np.sum(1/self.population[:,6])
        for i in range(self.N):
            self.population[i][7] = (1/self.population[i][6])/AntiSuma
        return AntiSuma
    def sort(self):
        for i in range(self.N):
            for j in range(1, self.N):
                if self.population[j-1][7] < self.population[j][7]:
                    self.population[j-1], self.population[j] = self.population[j], self.population[j-1]
    def generation(self):
        new_generation = []
        for i in range(int(self.N/2)):
            numbers = np.random.choice(range(self.N), 2, p = self.population[:, 7])
            cross = rn.randrange(1, 6)
            new_generation.append(np.concatenate([self.population[numbers[0], 0:cross], self.population[numbers[1], cross:8]]))
        new_generation = np.array(new_generation)
        self.population[int(self.N/2):self.N] = new_generation

    def mutation(self, Radiation):
        for i in range(Radiation):
            x = rn.randrange(0, self.N)
            y = rn.randrange(0, 6)
            self.population[x][y] += rn.random() * 2 - 1
    # def super_mutation(self, Radiation, Best):
    #     for i in range(Radiation):
    #         x = rn.randrange(1, self.N)
    #         for y in range(6):
    #             self.population[x][y] += (rn.random() - rn.random()) * 20

    #     for x in range(Best):
    #         y = rn.randrange(0, 6)
    #         self.population[x][y] += (rn.random() - rn.random()) * 0.5

