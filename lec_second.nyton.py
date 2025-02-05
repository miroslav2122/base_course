from
























x0 = 0
vx = v * np.cos(alpha) 
y0 = 0
vy0 = v * np.sin(alpha)

z0 = x0, vx0, y0, vy0
sol = odeint(move_func, z0, t)
