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
from matplotlib.lines import Line2D
from matplotlib import rcParams, cycler
from matplotlib import cm
import matplotlib.patches as mpatches
#url = "https://services.swpc.noaa.gov/json/dscovr/dscovr_mag_1s.json"
choice = int(input("1 = DSCOVR 1S, 2 = ACE 1H: "))
if choice == 1:
	url = "https://services.swpc.noaa.gov/json/dscovr/dscovr_mag_1s.json"
elif choice == 2:
	url = "https://services.swpc.noaa.gov/json/ace/mag/ace_mag_1h.json"
else: 
	print("Choose 1 or 2");
	exit()
data = requests.get(url).text
x = []
y = []
z = []
times = []
jsond = json.loads(data)
if choice == 2:
	numhours = int(input("How many hours to plot: "))
print(len(jsond))
#time.sleep(3)
j = 0
if choice == 2:
	for i in jsond[:numhours]:
		print(j)
		times.append(pd.to_datetime(i["time_tag"]))
		x.append(i["gsm_bx"])
		y.append(i["gsm_by"])
		z.append(i["gsm_bz"])
		j = j + 1
else:
	for i in jsond:
		print(j)
		times.append(pd.to_datetime(i["time_tag"]))
		x.append(i["bx_gsm"])
		y.append(i["by_gsm"])
		z.append(i["bz_gsm"])
		j = j + 1
#time = jsond[-1]["time_tag"]
print(times)
print(x)
print(y)
print(z)
#plt.plot(times,z)
#plt.ylim(-10,10)
#plt.show()
blue_patch = mpatches.Patch(color='blue', label='Bx')
red_patch = mpatches.Patch(color='red', label='By')
black_patch = mpatches.Patch(color='black', label='Bz')
fig = plt.figure()
ax = plt.axes()
ax.set_xlabel('Time')
ax.set_ylabel('Bz,Bx,By')
ax.plot(times,x, color='blue', marker='x')
ax.plot(times,y, color='red', marker='x')
ax.plot(times,z, color='black', marker='x')
ax.legend([blue_patch, red_patch, black_patch], ['Bx', 'By', 'Bz'])
plt.ylim(-10,10)
plt.savefig('latest.png')
plt.show()
