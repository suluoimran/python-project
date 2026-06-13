print("=============================")
print(" SMART WATER MANAGEMENT SYSTEM")
print("=============================")

# Function to calculate individual bills
def calculation_bill(previous, current):
    used_units = current - previous
    price_per_unit = 2.5 
    total_bills = used_units * price_per_unit
    return used_units, total_bills




#evaluation for high water usage
def evaluate_records(customer_records):
    print("\n=====================================")
    print("      HIGH USAGE EVALUATION REPORT    ")
    print("=====================================")
    
    high_users_count = 0
    
    for record in customer_records:
        # Check if the bill is greater than 100,000 Tsh
        if record['bill'] > 100000:
            print(f"!!! WARNING: {record['name']} (Meter: {record['meter']})")
            print(f"   - Water Used: {record['units']} units")
            print(f"   - Total Bill: Tsh {record['bill']:,}")
            print("    - Please check for leaks or minimize usage!\n")
            high_users_count = high_users_count + 1
            
    if high_users_count == 0:
        print("Good news! No customers exceeded the Tsh 100,000 bill.")
    



# Main program execution
customer_records = []

while True:
    # Customer details
    customer = input("\nENTER CUSTOMER NAME (or type 'exit' to finish):  ")
    if customer.lower() == 'exit':
        break
        
    meter_number = input("INSERT YOUR METER NUMBER (M.....):  ")

    # Amount of water used
    Previous_reading = float(input("ENTER YOUR PREVIOUS METER READING:  "))
    Current_reading = float(input("ENTER YOUR CURRENT METER READING:  "))

    # Calculate bill
    used_units, total_bills = calculation_bill(Previous_reading, Current_reading)

    # Save record as a small dictionary
    record = {
        "name": customer.title(),
        "meter": meter_number.upper(),
        "previous": Previous_reading,
        "current": Current_reading,
        "units": used_units,
        "bill": total_bills
    }
    
    # Append to records(small dictionary)
    customer_records.append(record)

    # Individual Summary Display
    print("\n--- CUSTOMER BILL SUMMARY ---")
    print(f"Customer Name:\t\t{record['name']}")
    print(f"Meter Number:\t\t{record['meter']}")
    print(f"Units Used:              {used_units}")
    print(f"TOTAL BILL:              Tsh {total_bills:,}") 
    print("-----------------------------")

# Run the evaluation after data entry is complete
if customer_records:
    evaluate_records(customer_records)
else:
    print("\nNo records were entered.")

print("\n===============================================")
print("THANK YOU FOR USING MY SMART WATER MANAGEMENT SYSTEM")
print("YOU ARE ALWAYS WELCOME AGAIN")
print("===============================================")
