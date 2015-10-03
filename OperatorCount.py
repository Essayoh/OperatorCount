import csv

remove_from = 4
remove_to = 10000

with open('olark_report_20150922_20150929.csv', 'rb') as fp_in, open("output.csv", "wb") as fp_out:
    reader = csv.reader(fp_in, delimiter=",")
    writer = csv.writer(fp_out, delimiter=",")
    for row in reader:
        del row[remove_from:remove_to]
        writer.writerow(row)

with open('output.csv') as week_in, open('output2.csv', "wb") as week_out:
	reader = csv.reader(week_in, delimiter=",")
	writer = csv.writer(week_out, delimiter=",")
	for row in reader:
		del row[1:3]
		writer.writerow(row)



# Pull in CSV from Olark w/ one week's information & create new CSV for output

# Drop all of the unused columns

# Break timestamps into days and hours

# Count number of operators with at least one chat in each hours

# Append hourly operator count to output CSV

