import numpy as np
import math
import matplotlib.pyplot as plt

# Where list_points(np.array) = [[3.7440e+01 5.4121e+02] [6.1218e+02 4.9432e+02]...[3.8130e+01 3.5315e+02]]
list_points = np.array([[3.7440e+01, 5.4121e+02], [6.1218e+02, 4.9432e+02], [3.8130e+01, 3.5315e+02]] )
positions = list_points
# Where t = [(0.9481610257893822, 37.44, 541.21), ..., (0.9313909810893908, 49.92, 541.44)]
t = [(0.9481610257893822, 37.44, 541.21), (0.95, 612.18, 494.32), (0.9313909810893908, 49.92, 541.44)]
x_sol = np.asarray(t) 

fig, ax = plt.subplots(2, figsize = (10,10), sharex=True, sharey=True)         # Prepare 2 plots
ax[0].set_title('Raw nodes')
ax[1].set_title('Optimized tour')
ax[0].scatter(positions[:, 0], positions[:, 1])             # plot A
ax[1].scatter(positions[:, 0], positions[:, 1])             # plot B
start_node = 0
for i in range(2):
    start_pos = positions[start_node]
    next_node = np.argmax(x_sol[start_node])
    end_pos = positions[next_node]
    ax[1].annotate("",
#            xy=start_pos, xycoords='data',
            xy=start_pos, xycoords='data',
            xytext=end_pos, textcoords='data',
            arrowprops=dict(arrowstyle="->",
                            connectionstyle="arc3"))
    start_node = next_node

plt.tight_layout()
plt.show()

exit()







radius = 1
dummy = np.zeros([8, 2])
dummy[:,0] = radius * np.sin(np.linspace(0, 2 * np.pi, num = 8)) + radius
dummy[:,1] = radius * np.cos(np.linspace(0, 2 * np.pi, num = 8)) + radius
print(dummy)

exit()

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()

x = np.arange(0, 2*np.pi, 0.01)
line, = ax.plot(x, np.sin(x))


def animate(i):
    line.set_ydata(np.sin(x + i / 50))  # update the data.
    return line,


ani = animation.FuncAnimation(
    fig, animate, interval=10, blit=True, save_count=50)

# To save the animation, use e.g.
#
# ani.save("movie.mp4")
#
# or
#
# writer = animation.FFMpegWriter(
#     fps=15, metadata=dict(artist='Me'), bitrate=1800)
# ani.save("movie.mp4", writer=writer)

plt.show()