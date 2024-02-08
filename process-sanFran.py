# Simple post-processing script to create a clean subset of tree data
#     - JRz, for personal use and not indended for real-world applications

#  NOTE: This is eliminating valid, useful data in lieu of something easier to visualize
#        It's possible that this will mask trends, as it is often VERY likely that missing data are non-randomly distributed (e.g. more missing data pre-1955 in this dataset)


import csv

def passes_filter(row):
    
    # Filter criteria:
    #   Only listed trees that have full species name supplied
    if int(row['year']) < 1950 :
        return False
    if int(row['year']) > 2022 :
        return False
    else:
        return True
    
    # think about what other filters you could run here...
# import and run passes_filter
data = []
header = []
with open('us-cities-history-table.csv','r') as f:
    reader = csv.DictReader(f)
    
    header = reader.fieldnames
    for row in reader:
        if passes_filter(row):
            # you might consider doing some additional processing here
            # e.g. splitting up qSpecies
            data.append(row)

print(len(data))

# export to new CSV       
with open('sanfran-pop-data','w') as f:
    writer = csv.DictWriter(f, fieldnames=header)
    writer.writeheader()
    writer.writerows(data)
