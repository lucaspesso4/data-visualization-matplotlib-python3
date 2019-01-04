import matplotlib.pyplot as plt

# data
x = [1, 2, 5]
y = [2, 3, 7]

# titles
plt.title('A Simple Line Graph')
plt.xlabel('X LABEL')
plt.ylabel('Y LABEL')

# graph functions
plt.plot(x, y)
plt.show()