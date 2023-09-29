import numpy as np
import matplotlib.pyplot as plt
import random as rn
from Population import Population
import time


file = open(r'C:\myProgram\py\Kolganov\input1.txt', 'r')
data = file.readlines()
for i in range(len(data)):
    data[i] = data[i].split(' ')
    while(True):
        try:
            data[i].remove('')
        except ValueError:
            break
mes = []
for i in range(len(data)):
    mes.append([float(data[i][0])/1000, float(data[i][1])/1000, float(data[i][2])/1000])
mes = np.array(mes)

start = time.time() ## точка отсчета времени

##код программы


pop = Population(600)
pop.calc_fitness()
pop.sort()
t = 0
errors = []
while(t<30 and pop.population[0][6]>0.0001):
    pop.calc_fitness()
    pop.sort()
    pop.generation()
    pop.calc_fitness()
    pop.sort()
    pop.mutation(800)
    pop.calc_fitness()
    pop.sort()
    #print(pop.population[0, 6].round(4))
    t += 1
    errors.append(pop.population[0, 6])
#print(pop.population[0, 6])

# for i in range(1000):
#     square_sum(mes, example):
print('dH1\t=\t{0:.4f}'.format(pop.population[0, 0]))
print('dH2\t=\t{0:.4f}'.format(pop.population[0, 1]))
print('dH3\t=\t{0:.4f}'.format(pop.population[0, 2]))
print('dK1\t=\t{0:.4f}'.format(pop.population[0, 3]))
print('dK2\t=\t{0:.4f}'.format(pop.population[0, 4]))
print('dK3\t=\t{0:.4f}'.format(pop.population[0, 5]))
plt.plot(range(len(errors)), errors, color = 'black')
plt.xlabel('Эпохи')
plt.ylabel('Сумма квадратов ошибок для лучшей особи')
plt.grid()
plt.show()

end = time.time() - start ## собственно время работы программы

print(end) ## вывод времени
Suma = (((i[0] - dH1)/(1 + dK1))**2 + ((i[1] - dH2)/(1 + dK2))**2 + ((i[2] - dH3)/(1 + dK3))**2)
print(((H1-dH1)/(1+dK1))**2 + ((H2-dH2)/(1+dK2))**2 + ((H3-dH3)/(1+dK3))**2)