import matplotlib.pyplot as plt

# data
x = [1, 2, 3, 4, 5]
y = [2, 3, 7, 1, 9]

# titles
graph_title = 'A Simple Title Here'
x_title = 'X Title'
y_title = 'Y Title'

plt.title(graph_title)
plt.xlabel(x_title)
plt.ylabel(y_title)

# graph functions
plt.bar(x, y)
plt.show()