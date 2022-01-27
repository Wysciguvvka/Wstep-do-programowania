import matplotlib.pyplot as plt
import csv
from datetime import datetime

with open('dane-meteo-grow-green-pre-greening.csv', 'r', encoding="utf-8") as csvfile:
    lines = csv.reader(csvfile, delimiter=';')
    next(lines)
    temperature = {}
    wind = {}
    precipitation = {}
    rainydays = [0, 0]
    samples = 0
    x, y = [], []
    humidity_x, humidity_y = [], []
    for row in lines:
        try:
            date = f'{row[0]}-{row[1]}-{row[2]}'
            if date in temperature:
                temperature[date].append(float(row[4].replace(',', '.')))
            else:
                samples += 1
                temperature[date] = [float(row[4].replace(',', '.'))]
        except ValueError:
            pass
        try:
            if not row[0]:
                continue
            date = f'{row[0]}-{row[1]}-{row[2]}'
            if date in precipitation:
                precipitation[date] += 1 if row[6].strip() else 0
            else:
                if not row[6].strip():
                    continue
                precipitation[date] = 1
        except ValueError:
            pass
        try:
            date = f'{row[0]}-{row[1]}'
            if date in wind:
                wind[date].append(float(row[5].replace(',', '.')))
            else:
                wind[date] = [float(row[5].replace(',', '.'))]
        except ValueError:
            pass
    for key, item in temperature.items():
        avg = int(sum(item) / len(item))
        x.append(datetime.strptime(key, '%Y-%m-%d'))
        y.append(avg)
    for key, item in wind.items():
        avg = float(sum(item) / len(item))
        humidity_x.append(datetime.strptime(key, '%Y-%m'))
        humidity_y.append(avg)

fig, axs = plt.subplots(2, 2)
rainydays[0] = len(precipitation.values())
rainydays[1] = samples - rainydays[0]
axs[0, 0].pie(rainydays, autopct='%1.1f%%', colors=['#FDBB2F', '#007CC3'])
axs[0, 0].set_title("Percent of rainy days (1 year)")
axs[0, 0].legend(["Clear Days", "Rainy days"], bbox_to_anchor=(1, 1))

axs[0, 1].set_title("Precipitation duration")
axs[0, 1].hist(precipitation.values(), 20, linewidth=0.5, edgecolor='black')
axs[0, 1].set_xlabel("Duration in hours")
axs[0, 1].set_ylabel("Occurences")

axs[1, 0].plot(x, y, 'tab:green')
axs[1, 0].set_title('Average Daily Temperature')
axs[1, 0].set_xlabel("Time")
axs[1, 0].set_ylabel("Temperature (°C)")

axs[1, 1].set_title("Average wind speed per month")
axs[1, 1].plot(humidity_x, humidity_y, alpha=0.5, color="#4421af")
axs[1, 1].scatter(humidity_x, humidity_y, alpha=1, linestyle='solid', s=20, color="#4421af")
axs[1, 1].set_xlabel("Time")
axs[1, 1].set_ylabel("wind speed [m/s]")

plt.setp(axs[1, 0].get_xticklabels(), rotation=20, horizontalalignment='right', fontsize='x-small')
plt.setp(axs[1, 1].get_xticklabels(), rotation=20, horizontalalignment='right', fontsize='x-small')
# plt.setp(axs[0, 1].get_xticklabels(), rotation=20, horizontalalignment='right', fontsize='x-small')
plt.setp(axs[0, 0].get_xticklabels(), rotation=20, horizontalalignment='right', fontsize='x-small')
plt.tight_layout()
plt.show()
