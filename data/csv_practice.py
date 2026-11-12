print ("Exercise 1 - Setup")


print ("Exercise 2 - Read and print raw rows")
import csv
with open("data/sales.csv", "r", newline="") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

print ("Exercise 3 - Skip the header")
