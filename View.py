#de view van de applicatie: grafieken etc en eerste scherm com devices
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

style.use('ggplot')

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
xs = []
ys = []
y2 = []

def animate(i):
    graph_data = open('sensordata.txt','r').read()
    lines = graph_data.split('\n')
    for line in lines:
        if len(line)>1:
            x,y,z = line.split(',')
            xs.append(int(x))
            ys.append(int(y))
            y2.append(int(z))
    ax1.clear()
    plt.xlabel('min.')
    ax1.plot(xs,ys,label='temperatuur')
    ax1.plot(xs,y2,label='licht')
    plt.legend()

ani = animation.FuncAnimation(fig, animate, interval=60000)


