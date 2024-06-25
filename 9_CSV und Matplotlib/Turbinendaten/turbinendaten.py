import csv


turbinedata=[]

with open('10m.csv','r') as csv_file:
    csv_reader =csv.reader(csv_file)

    next(csv_reader)

    for line in csv_reader:
        turbinedata.append(line)


print(turbinedata)

winddata=[x[0] for x in turbinedata]
print()
print(winddata)
wdsplit=[str(x).split(";") for x in winddata]
print()
print(wdsplit)
avgWind=[float(x[0]) for x in wdsplit]
print()
print(avgWind)
avgPower=[float(x[3])/200 for x in wdsplit]
print()
print(avgWind, "\n", avgPower)


from matplotlib import pyplot as plt

axx=[x for x in range(144)]

plt.plot(axx, avgWind, avgPower)

plt.show()