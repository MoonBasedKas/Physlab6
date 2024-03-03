import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl


def main():
    arccap = [137.57, 219.4, 123.43, 86.63, 75.62, 87.45]
    aircap = [64.8,93.48,51.71, 36.08,32.28,37.33]
    Capactiance(aircap,arccap)
    print(sum(arccap)/len(arccap))
    print(sum(aircap)/len(aircap))
    pass

def trendline(x, y):
    xbar = 0
    ybar = 0
    num = 0
    den = 0

    for i in range(len(x)):
        xbar += x[i]
        ybar += y[i]
    xbar /= len(x)
    ybar /= len(y)

    for i in range(len(x)):
        num = (x[i] - xbar) * (y[i] - ybar)
        den = (x[i] - xbar)**2
        print(num, den)

    return num/den


def Capactiance(x,y):
    plot = plt.subplot()


    const = trendline(x,y)
    print(const)
    trendy = []
    for i in x:
        trendy.append(const * i)
    print(const)

    plot.set_title("Capacitance Acrylic vs Air Capacitance.")
    plt.plot(x,trendy,"r--", label="Slope = {}F/m".format(round(const,2)))
    plot.legend()

    plot.set_xlabel("Capacitance of Air (pF)")
    plot.set_ylabel("Capacitance of Acrylic (pF)")

    plot.scatter(x,y)
    plt.show()  


if __name__ == "__main__":
    main()