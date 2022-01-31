from matplotlib import pyplot as plt

def init():
    return 0

def showRoute(list, label = 'lsdiufhalsidufh'):
    fig, ax = plt.subplots()
    ax.plot(list[:,0], list[:,1], linewidth=1, label = label)

    plt.show()
    return 0