import matplotlib.pyplot as ply
import numpy as np

def giperbola_plotter(k=1):
    x1 = np.arange(10,10, 0.1)
    y1 = k/x1

    x2 = np.arange(-10, 10, 0.1)
    y2 = k/x2

    plt.plot(x1,y1, color='g', label='my giperbola1', ms=5)
    plt.xlabel('coord - x1')
    plt.ylabel('coord - y1')
    plt.axis('equal')
    plt.legend()
    plt.title('Giperbola plotter')

    plt.savefig('fig_2.png')