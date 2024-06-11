import csv


turbinedata=[]

with open('10m.csv','r') as csv_file:
    csv_reader =csv.reader(csv_file)

    next(csv_reader)

    for line in csv_reader:
        turbinedata.append(line)


#print(turbinedata)

winddata=[x[0] for x in turbinedata]
#print(winddata)
wdsplit=[str(x).split(";") for x in winddata]
#print(wdsplit)
avgWind=[float(x[0]) for x in wdsplit]
#print(avgWind)
avgPower=[float(x[3])/200 for x in wdsplit]
#print(avgWind, "\n", avgPower)

""" with open('D:\\Projekte\\Softwareprojekte\\Python\\LG2\\10m.csv','r') as csv_file:
    csv_reader =csv.DictReader(csv_file, delimiter=';')

    for line in csv_reader:
        print(line['Wind Speed (avg)']) """


from matplotlib import pyplot as plt

axx=[x for x in range(144)]

plt.plot(axx, avgWind, avgPower)

plt.show()