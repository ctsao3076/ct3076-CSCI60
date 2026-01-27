import csv

def load_csv(filepath):
    data= []

    with open(filepath, newline="", encoding= "utf-8") as f:
        reader= csv.DictReader(f)
        for row in reader:
            data.append(row)

    return data

blocks= load_csv("Block_Planting.csv")

#task 1: print the first two rows
print(blocks[:21])

#task 2: print the first row
print(blocks[:0])

#task 3: print rows 10-19
print(blocks[10:20])

#task 4: print column names
print(list(blocks[0].keys()))

#task 5 print the first ten values of one column
for row in blocks[:10]:
    print(row["Status"])

#task 6: print the first ten rows of three columns
for row in blocks[:10]:
    print(row["PHYSICALID"], row["BOROUGHCODE"], row["BlkPlnt"])


