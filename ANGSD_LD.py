# Author: C. Isabel Wagner, Nord University Bodø Norway, 2023
import csv

dct=dict()
for i in range(467,507):
    dct["NC_054"+str(i)+".1"]=list()

print("Reading position data")
current="lala"
with open("forngsLD.GWSsamtoolsGL6.mafs", "r",newline='') as infile:
    tsvreader = csv.reader(infile, delimiter='\t')
    for row in tsvreader:
        line=list(row)
        if line[0] in dct.keys():
            if current!=line[0]:
                current=line[0]
                dct[line[0]]+=[line[1]]
                dist=int(line[1])
            else:
                if int(line[1])>(dist+999):
                    dct[line[0]]+=[line[1]]
                    dist=int(line[1])

print("Thinning")
with open("../forngsLD.GWSsamtoolsGL3.LD.tsv", "r",newline='') as infile:
    with open("1kbdist_13indv_forngsLD.GWSsamtoolsGL3.LD.tsv", "w",newline='') as outfile:
        tsvreader = csv.reader(infile, delimiter='\t')
        tsvwriter = csv.writer(outfile, delimiter='\t')
        for row in tsvreader:
            line=list(row)
            if (line[1]).split(":")[0] in dct.keys():
                if (line[0]).split(":")[1] in dct[(line[1]).split(":")[0]] and (line[1]).split(":")[1] in dct[(line[1]).split(":")[0]]:
                    tsvwriter.writerow(line)
