import csv
import os

timestamps = []
rawdates = []
dates = []
rawtimes = []
times = []
opers = []
timelist = ['00','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24']

#import Olark file, pull timestamps and operators

with open('olark_report_20150922_20150929.csv', 'rb') as olark_in:
    reader = csv.reader(olark_in, delimiter=',')
    for row in reader:
        timestamps.append(row[0])
        opers.append(row[3])

#splitting time and date

for i in timestamps:
	rawdates.append(i.split(' ',1)[0])
	rawtimes.append(i.split(' ',1)[-1])

#deleting headers

del timestamps[0], rawdates[0], rawtimes[0], opers[0]

#formatting dates

for i in rawdates:
	if i not in dates:
		dates.append(i)

dates.reverse()

#formatting times

for i in rawtimes:
	times.append(i.split(':',1)[0])

#exporting to new .csv

with open('output.csv', 'wb') as olark_out:
	writer = csv.writer(olark_out, delimiter = ',')
	for date in dates:
			writer.writerow([date])


# Count number of operators with at least one chat in each hours

