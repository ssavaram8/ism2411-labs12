print("Exercise 1: Setup") #!!!

print("Exercise 2: Read and print raw rows") #!!!

import csv
with open("data/sales.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

print("Exercise 3: Skip the header") #!!!

with open("data/sales.csv", "r") as f:
    reader = csv.reader(f)
    header = next(reader)  
    for row in reader:
        print(row)
    print("Header:", header)

print("Exercise 4: Compute totals") #!!!

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

print("Exercise 5: Filter + Write") #!!!

high_value = []
rows_read = []

with open ("data/sales.csv", "r") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader: 
        rows_read += 1
        product, price_str, qty_str = row
        price = float(price_str)
        qty = int(qty_str)
        revenue = price * qty
        if revenue > 100:
            high_value.append((product, f"{price:.2f}", qty, f"{revenue:.2f}"))

with open("data/clean.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["product", "price", "quantity", "revenue"])
    writer.writerows(high_value)
    for row in high_value:
        writer.writerow(row)

print(f"highest value: {len(high_value)} rows written to clean.csv")
print(f"total rows read: {rows_read} rows written to clean.csv")

print("Exercise 6: csv.DictReader") #!!!

dict_total = 0
with open("data/sales.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        product = row["product"]
        price = float(row["price"])
        qty = int(row["quantity"])
        revenue = price * qty
        dict_total += revenue
        print(f"{product}: {qty} units × ${price:.2f} = ${revenue:.2f}")

print("Exercise 7: Sales summary by product") #!!!

