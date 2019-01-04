# Brazilian Population Growth 1980 - 2016

import matplotlib.pyplot as plt

# data
data = open('brazilian-population.csv').readlines()
year = []
population = []

for i in range(len(data)):
    if i != 0:
        line = data[i].split(';')
        year.append(int(line[0]))
        population.append(int(line[1]))

# titles
plt.title('Brazilian Population Growth 1980 - 2016')
plt.xlabel('Year')
plt.ylabel('Population x100.000.000')

# graph
plt.bar(year, population, color = "#e4e4e4")
plt.plot(year, population, color = "k", linestyle = "--")
plt.show()