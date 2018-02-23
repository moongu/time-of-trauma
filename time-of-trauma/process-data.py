import csv, time

infile = open('time-of-crime-processed.csv','rb')
outfile = open('time-of-crime-minute-to-date.csv','wb')
reader = csv.reader(infile)
writer = csv.writer(outfile)

for row in reader:
	"""
    if not row[13]==0: #ignore nonsubscribers
        if row[1].split(" ")[0]=="11/1/2015":
            newrow = (row[1].split(" ")[1],row[2].split(" ")[1],row[5],row[6],row[9],row[10])
            writer.writerow(newrow)
    """

infile.close()
outfile.close()