import numpy as np
import matplotlib.pyplot as plt
import urllib
import time
import matplotlib.animation as anim
import matplotlib.mlab as mlab
from scipy.stats import norm

fig1 = plt.figure(1)
fig2 = plt.figure(2)


def animatef1(i):
    try:
        print 'Downloading File...'

        urllib.urlretrieve("https://api.thingspeak.com/stream/channels/268226/feeds?api_key=BW7SHPGTJ6ES0OTB&timezone=UTC", "feeds.csv")
        print 'Done!'

    
        global x, temp, hum, bar, dew, cloud, ir, length, startvalue

    
    
        data = np.genfromtxt('feeds.csv', delimiter=',', skip_header=1, names=['created_at', 'entry_id', 'temp', 'hum', 'bar', 'dew', 'cloud', 'ir'])
        x = data['entry_id']
        temp = data['temp']
        hum = data['hum']
        bar = data['bar']
        dew = data['dew']
        cloud = data['cloud']
        ir = data['ir']

        length = len(x)
        lastvalues = 2000
        startvalue = length - lastvalues


    

        ax1 = fig1.add_subplot(3,2,1)
        ax1.clear()
        ax1.plot(x[startvalue:length], temp[startvalue:length],'b-')
        ax1.set_xlabel('Entry ID')
        ax1.set_ylabel('Temperature', color='b')
        ax1.text(x[-1] + 50, temp[-1], temp[-1], color='b', bbox={'facecolor':'white', 'edgecolor':'none', 'pad':1} )
        ax1.tick_params('y', colors='b')
        ax1.grid(True)

        ax2 = fig1.add_subplot(3,2,2)
        ax2.clear()
        ax2.plot(x[startvalue:length], hum[startvalue:length],'b-')
        ax2.set_xlabel('Entry ID')
        ax2.set_ylabel('Humidity', color='b')
        ax2.text(x[-1] + 50, hum[-1], hum[-1], color='b', bbox={'facecolor':'white', 'edgecolor':'none', 'pad':1} )    
        ax2.tick_params('y', colors='b')
        ax2.grid(True)

        ax5 = fig1.add_subplot(3,2,3)
        ax5.clear()
        ax5.plot(x[startvalue:length], cloud[startvalue:length],'r-')
        ax5.set_xlabel('Entry ID')
        ax5.set_ylabel('Cloud Base', color='r')
        ax5.text(x[-1] + 50, cloud[-1], cloud[-1], color='r', bbox={'facecolor':'white', 'edgecolor':'none', 'pad':1} )
        ax5.tick_params('y', colors='r')
        ax5.grid(True)



        ax4 = fig1.add_subplot(3,2,4)
        ax4.clear()
        ax4.plot(x[startvalue:length], dew[startvalue:length],'r-')
        ax4.set_xlabel('Entry ID')
        ax4.set_ylabel('Dew Point', color='r')
        ax4.text(x[-1] + 50, dew[-1], dew[-1], color='r', bbox={'facecolor':'white', 'edgecolor':'none', 'pad':1} )
        ax4.tick_params('y', colors='r')
        ax4.grid(True)

        ax3 = fig1.add_subplot(3,2,5)
        ax3.clear()
        ax3.plot(x[startvalue:length], bar[startvalue:length],'b-')
        ax3.set_xlabel('Entry ID')
        ax3.set_ylabel('Barometric Pressure', color='b')
        ax3.text(x[-1] + 50, bar[-1], bar[-1], color='b', bbox={'facecolor':'white', 'edgecolor':'none', 'pad':1} )
        ax3.tick_params('y', colors='b')
        ax3.grid(True)

        ax6 = fig1.add_subplot(3,2,6)
        ax6.clear()
        ax6.plot(x[startvalue:length], ir[startvalue:length],'b-')
        ax6.set_xlabel('Entry ID')
        ax6.set_ylabel('IR Irradiance', color='b')
        ax6.text(x[-1] + 50, ir[-1], ir[-1], color='b', bbox={'facecolor':'white', 'edgecolor':'none', 'pad':1} )
        ax6.tick_params('y', colors='b')
        ax6.grid(True)
        fig1.savefig('full_figure.png')
    except:
        print 'Error1. Reloading'
        pass


def animatef2(i):
    try:
        ax1_f2 = fig2.add_subplot(3,2,1)
        ax1_f2.clear()
        n1, bins1, patches1 = ax1_f2.hist(temp[startvalue:length], 30, normed=1, facecolor='blue', alpha=0.75)
        (mu1, sigma1) = norm.fit(temp[startvalue:length])
        y1 = mlab.normpdf( bins1, mu1, sigma1)
        l1 = ax1_f2.plot(bins1, y1, 'r--', linewidth=2)
        ax1_f2.grid(True)
    
        ax2_f2 = fig2.add_subplot(3,2,2)
        ax2_f2.clear()
        n2, bins2, patches2 = ax2_f2.hist(hum[startvalue:length], 30, normed=1, facecolor='blue', alpha=0.75)
        (mu2, sigma2) = norm.fit(hum[startvalue:length])
        y2 = mlab.normpdf( bins2, mu2, sigma2)
        l2 = ax2_f2.plot(bins2, y2, 'r--', linewidth=2)
        ax2_f2.grid(True)

        ax3_f2 = fig2.add_subplot(3,2,3)
        ax3_f2.clear()
        n3, bins3, patches3 = ax3_f2.hist(cloud[startvalue:length], 30, normed=1, facecolor='red', alpha=0.75)
        (mu3, sigma3) = norm.fit(cloud[startvalue:length])
        y3 = mlab.normpdf( bins3, mu3, sigma3)
        l3 = ax3_f2.plot(bins3, y3, 'b--', linewidth=2)
        ax3_f2.grid(True)

        ax4_f2 = fig2.add_subplot(3,2,4)
        ax4_f2.clear()
        n4, bins4, patches4 = ax4_f2.hist(dew[startvalue:length], 30, normed=1, facecolor='red', alpha=0.75)
        (mu4, sigma4) = norm.fit(dew[startvalue:length])
        y4 = mlab.normpdf( bins4, mu4, sigma4)
        l4 = ax4_f2.plot(bins4, y4, 'b--', linewidth=2)
        ax4_f2.grid(True)

        ax5_f2 = fig2.add_subplot(3,2,5)
        ax5_f2.clear()
        n5, bins5, patches5 = ax5_f2.hist(bar[startvalue:length], 30, normed=1, facecolor='blue', alpha=0.75)
        (mu5, sigma5) = norm.fit(bar[startvalue:length])
        y5 = mlab.normpdf( bins5, mu5, sigma5)
        l5 = ax5_f2.plot(bins5, y5, 'r--', linewidth=2)
        ax5_f2.grid(True)

        ax6_f2 = fig2.add_subplot(3,2,6)
        ax6_f2.clear()
        n6, bins6, patches6 = ax6_f2.hist(ir[startvalue:length], 30, normed=1, facecolor='blue', alpha=0.75)
        (mu6, sigma6) = norm.fit(ir[startvalue:length])
        y6 = mlab.normpdf( bins6, mu6, sigma6)
        l6 = ax6_f2.plot(bins6, y6, 'r--', linewidth=2)
        ax6_f2.grid(True)
        fig2.savefig('full_figure2.png')
    except:
        print 'Error2. Reloading'
        pass

animatef1(1)
animatef2(1)

fig1.subplots_adjust(left=0.11, bottom=0.11, right=0.93, top=0.96, wspace=0.54, hspace=0.55)
fig2.tight_layout()
#plt.tight_layout()
anf1 = anim.FuncAnimation(fig1, animatef1, interval=45000)
anf2 = anim.FuncAnimation(fig2, animatef2, interval=45000)
plt.show()

