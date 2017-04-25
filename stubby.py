
import sys
import csv
from random import randint
from os.path import expanduser
#home = expanduser("~")

import csv

with open(sys.argv[2],'r') as csvinput:
    with open(sys.argv[3], 'w') as csvoutput:
        writer = csv.writer(csvoutput, lineterminator='\n')
        reader = csv.reader(csvinput)

        all = []
        row = next(reader)
        row.append("Assigned Team")
        all.append(row)

		#if ((len(csvinput)-1)%3 == 0) :
		#    rando = randint(1, (len(csvinput)-1)/3)
		#else:
		#    rando = randint(1, round((len(csvinput)-1)/3))
            
        for row in reader:
            row.append(randint(1, round((len(csvinput)-1)/3)))
            all.append(row)

        writer.writerows(all)
		
	csvoutput.close()
	
csvinput.close()
