import json
import matplotlib as mpl
import re
import requests
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt 
from datetime import timedelta
import pandas as pd
from datetime import datetime
import time 



#url = "https://services.swpc.noaa.gov/json/dscovr/dscovr_mag_1s.json"
url = "https://services.swpc.noaa.gov/json/ace/mag/ace_mag_1h.json"
data = requests.get(url).text
x = []
y = []
z = []
times = []
jsond = json.loads(data)
numhours = int(input("How many hours to plot: "))
timestampw = input("Do you want timestamps? y or n:")
if timestampw != 'y' and timestampw != 'n':
	print("Please provide a lowercase y or n")
	exit()
print(len(jsond))
#time.sleep(3)
j = 0
for i in jsond[:numhours]:
	print(j)
	times.append(pd.to_datetime(i["time_tag"]))
	x.append(i["gsm_bx"])
	y.append(i["gsm_by"])
	z.append(i["gsm_bz"])
	j = j + 1

#time = jsond[-1]["time_tag"]
print(times)
print(x)
print(y)
print(z)
#plt.plot(times,z)
#plt.show()
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.axes.set_xlim3d(left=-10,right=10)
ax.axes.set_ylim3d(bottom=-10,top=10)
ax.axes.set_zlim3d(bottom=-10,top=10)
ax.set_xlabel('Bx')
ax.set_ylabel('By')
ax.set_zlabel('Bz')
ax.plot3D(x,y,z,'blue', marker='x')
if timestampw == 'y':
	for i in range(len(x)):
		ax.text(x[i], y[i], z[i], times[i])
else:
	pass
plt.show()
