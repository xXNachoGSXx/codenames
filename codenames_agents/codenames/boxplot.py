import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import csv

data_rows = []
columns = []
plot_data = []

#import from the csv
with open('30exp_results.csv') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')
	line = 0
	for row in csv_reader:
		if line == 0:
			columns = row
		else:
			data_rows.append(row)
		line+=1

for d in data_rows:
	dlist = [int(v) for v in d[3:]]
	plot_data.append(dlist)

print(plot_data)

#create the box plot
fig = plt.figure(1,figsize=(10,6))
ax = fig.add_subplot(111)
bp = ax.boxplot(plot_data)
plt.show()
