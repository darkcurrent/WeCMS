import numpy as np
import matplotlib.pyplot as plt
import urllib
print 'Downloading File...'
urllib.urlretrieve("https://api.thingspeak.com/stream/channels/268226/feeds?api_key=BW7SHPGTJ6ES0OTB&timezone=UTC", "feeds.csv")
print 'Done!'
data = np.genfromtxt('feeds.csv', delimiter=',', skip_header=1, names=['created_at', 'entry_id', 'temp', 'hum', 'bar', 'dew', 'cloud', 'ir'])
x = data['ir']
y1 = data['temp']
y2 = data['hum']
length = len(x)
lastvalues = 2000
startvalue = length - lastvalues

fig1 = plt.figure()
#fig, ax1 = plt.subplots()

ax1 = fig1.add_subplot(211)
ax1.scatter(x[startvalue:length], y1[startvalue:length],s=2,c='b')
ax1.set_xlabel('ir')
ax1.set_ylabel('temp', color='b')
ax1.tick_params('y', colors='b')

ax2 = ax1.twinx()
ax2.scatter(x[startvalue:length], y2[startvalue:length],s=2,c='r')
ax2.set_ylabel('hum', color='r')
ax2.tick_params('y', colors='r')
ax3 = fig1.add_subplot(212)
ax3.plot(1,1,'r.-')

fig1.tight_layout()
plt.show()

