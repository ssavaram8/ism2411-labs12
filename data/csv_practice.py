print ("Exercise 1 - Setup")

print ("Exercise 2 - Read and print raw rows")

import csv
with open("data/sales.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

print ("Exercise 3 - Skip the header")

with open("data/sales.csv", "r") as f:
    reader = csv.reader(f)
    header = next(reader)  
    for row in reader:
        print(row)
    print("Header:", header)

print ("Exercise 4 - Compute totals") 

total = []

with open("data/sales.csv", "r") as f:
    reader = csv.reader(f)
    header = next(reader)
    print("Header:", header)

    for row in reader:
        product = row[0]
        price = float(row[1])
        qty = int(row[2])
        revenue = price * qty

        total.append(revenue)
        print(f"{product}: {qty} units × ${price:.2f} = ${revenue:.2f}")

print(f"total revenue: ${sum(total):.2f}")

