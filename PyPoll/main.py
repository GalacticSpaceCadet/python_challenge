#import the needed modules and set path
import os
csvpath = os.path.join('election_data_1.csv')

import csv
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)

    count = 0
    counts = {}
    

    #  Each row is read as a row
    for row in csvreader:
        count += 1
        if (row[2] in counts.keys()):
            counts[row[2]] +=1
        else:
            counts[row[2]] = 1
        #print(row[0])
        # print (len(idcount)

    #count total rows

    print(row)

    #countal total instances of names

    #calculate percentge
        

