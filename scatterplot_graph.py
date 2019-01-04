import matplotlib.pyplot as plt

# data
x = [1, 3, 5, 7, 9]
y = [2, 3, 7, 1, 9]

# titles
graph_title = 'A Simple Title Here'
x_title = 'X Title'
y_title = 'Y Title'

plt.title(graph_title)
plt.xlabel(x_title)
plt.ylabel(y_title)

# graph functions
plt.scatter(x, y, label = "Dots", color = "r")
plt.legend()
plt.plot(x,y)
plt.show()
# plt.savefig('filename.png') or .pdf dpi = ANYNUMBERHERE