import matplotlib.pyplot as plt
import numpy as np

def hyperbola_plotter(k=1):
    x1 = np.arange(-10, -0.01, -0.1)
    y1 = k/x1
    x2 = np.arange(0.01, 10, 0.1)
    y2 = k/x2

    plt.plot(x1,y1, color='g', label='my hyperbola1', ms=5)
    plt.xlabel('coord - x1')
    plt.ylabel('coord - y1')
    plt.axis('equal')
    plt.legend()
    plt.title('Giperbola plotter')

if __name__=='__main__':
    hyperbola_plotter() 
    plt.savefig('fig_2.png')