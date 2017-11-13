#de view van de applicatie: grafieken etc en eerste scherm com devices
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

import settings

style.use('ggplot')
fig = plt.figure()
def animate(i):


    data = settings.com_list[0].get_temp_licht(settings.com_list[0].info)
    data = str(data)
    temp = data[0:2]
    licht = data[2:4]
    temp = int(temp, 16)
    licht = int(licht, 16)
    data_r = open('sensordata.txt', 'r')
    print(temp, licht)
    count = 1;
    for i in data_r:
        count += 1
    data_r.close()
    data_w = open('sensordata.txt', 'a')
    if temp != 0:
        data_w.write('{},{},{} \n'.format(count, temp, licht))
        data_w.close

    ax1 = fig.add_subplot(1, 1, 1)
    xs = []
    ys = []
    y2 = []
    
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
    ax1.plot(xs,ys,label='licht')
    ax1.plot(xs,y2,label='temperatuur')
    plt.legend()

ani = animation.FuncAnimation(fig, animate, interval=60000)


