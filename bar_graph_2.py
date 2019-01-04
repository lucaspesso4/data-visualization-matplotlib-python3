import matplotlib.pyplot as plt

# data
x1 = [1, 3, 5, 7, 9]
y1 = [2, 3, 7, 1, 9]

x2 = [2, 4, 6, 8, 10]
y2 = [5, 1, 3, 7, 4]

# titles
graph_title = 'A Simple Title Here'
x_title = 'X Title'
y_title = 'Y Title'

plt.title(graph_title)
plt.xlabel(x_title)
plt.ylabel(y_title)

# graph functions
plt.bar(x1, y1, label = "Group 1")
plt.bar(x2, y2, label = "Group 2")
plt.legend() # adding legends
plt.show()