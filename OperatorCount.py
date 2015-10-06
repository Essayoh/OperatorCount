import csv
import os

timestamps = []
rawdates = []
dates = []
rawtimes = []
times = []
opers = []
timelist = ['00','01','02','03','04','05','06','07',
			'08','09','10','11','12','13','14','15',
			'16','17','18','19','20','21','22','23']
csvoutput = []


#import Olark file, pull timestamps and operators

with open('olark_report_20150922_20150929.csv', 'rb') as olark_in:
    reader = csv.reader(olark_in, delimiter=',')
    for row in reader:
        timestamps.append(row[0])
        opers.append(row[3])

#create output file and headers

with open('output.csv', 'wb') as output:
	writer = csv.writer(output, delimiter=',')
	writer.writerow(['Date','00','01','02','03','04','05','06','07'
					  ,'08','09','10','11','12','13','14','15','16',
					   '17','18','19','20','21','22','23'])

#splitting time and date

for i in timestamps:
	rawdates.append(i.split(' ',1)[0])
	rawtimes.append(i.split(' ',1)[-1])

#deleting headers

del timestamps[0], rawdates[0], rawtimes[0], opers[0]

#formatting dates & times

for i in rawdates:
	if i not in dates:
		dates.append(i)

print dates

dates.reverse()
csvoutput.append(dates)

for i in rawtimes:
	times.append(int(i.split(':',1)[0]))

#formatting data - need 7 columns of 24 values each
#so need to check and count for each hour and output operator count
#maybe an array - date: hour:count, so each date will have 24 hour:count key:value pairs


#using rawdates here b/c dates has only 7 entries and won't map onto full data, only first 7 entries
workdata = zip(rawdates,times,opers)

count = 00
array = [


]

for i in workdata:
	if i[1] == count:
		opcount.append(i[2])

len(set(opcount))


		




#exporting to new .csv

#with open('output.csv', 'wb') as olark_out:
#	writer = csv.writer(olark_out, delimiter = ',')
#	for date in dates:
#			writer.writerow([date])

