import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt

df = pd.read_csv('all.csv', sep=';', decimal=',')

x = df['xi'].to_numpy()
y = df['yi'].to_numpy()
# for i in range(1,30):
#     z = df[str(i)].to_numpy()

#     fig = plt.figure()
#     ax = plt.axes(projection='3d')

#     ax.scatter(x, y, z, c=z, cmap='Greens')
#     plt.show()

z = df['17'].to_numpy()

b1 = -20.08858467
b2 = -3.71427772
b3 = 1.21821486

X,Y = np.meshgrid(np.linspace(0,20,len(x)), np.linspace(0,10,len(x)))
Z = b1 + b2*(Y**2) + b3*X*Y

fig = plt.figure(figsize=(6,6))
ax = fig.add_subplot(111, projection='3d')

# Plot a 3D surface
ax.plot_surface(X, Y, Z)
# ax = plt.axes(projection='3d')
ax.scatter(x, y, z, c=z, cmap='Greens')
plt.show()
