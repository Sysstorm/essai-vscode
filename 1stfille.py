import matplotlib.pyplot as plt

x=[i for i in range (1,10)]

print(x)

plt.plot(x,[i*3 for i in x])
plt.title("nouveau graph")
plt.show()