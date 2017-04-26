

import sys
import csv
from random import randint
from os.path import expanduser
#home = expanduser("~")

import csv
print (sys.argv[1])
print (sys.argv[2])

with open(sys.argv[1],'r') as csvinput:
    with open(sys.argv[2], "w") as csvoutput:
        writer = csv.writer(csvoutput, lineterminator='\n')
        reader = csv.reader(csvinput)
        csv_list = list(reader)
        
        all = []
        
        row = csv_list[0]
        cList = iter(csv_list)
        #row = csv_list.next()
        row.append("Assigned Team")
        all.append(row)

        #if ((len(csvinput)-1)%3 == 0) :
        #    rando = randint(1, (len(csvinput)-1)/3)
        #else:
        #    rando = randint(1, round((len(csvinput)-1)/3))
        teamSize = round((len(csv_list)-1)/3)
        next(cList)
        for row in cList:
            row.append(randint(1, teamSize))
            all.append(row)

        writer.writerows(all)
        
    csvoutput.close()
    
csvinput.close()
