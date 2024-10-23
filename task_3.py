import numpy as np
x0 = 0
v0 = 20
y0 = 0

d = 45
r = np.radians(d)

v0x = v0*np.cos(r)
v0y = v0 * np.sin(r)

g = 10

t = np.linspace(0, 5, 100)

x = x0 + v0y * t 
y = y0 + v0y * t - 0.5 * g * (t ** 2)

res = np.column_stack((t,x,y))
print(res)