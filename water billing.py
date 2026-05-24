print("=============================")
print("SIMPLE WATER BILLING SYSTEM")
print("=============================")

# Customer details
customer=input("ENTER CUSTOMER NAME: ")
meter_number=input("INSERT YOUR METER NUMBER(M.....):  ")

# AMOUNT OF WATER USED
Previous_reading=float(input("ENTER YOUR PREVIOUS METER READING: "))
Current_reading=float(input("ENTER YOUR CURRENT METER READING:  "))

# FUNCTION FOR CALCULATION
def calculation_bill(previous,current):
    used_units=current -previous
    price_per_unit=2.5 
    total_bills=used_units * price_per_unit
    return used_units,total_bills

# FUNCTION CALLS
used_units,total_bills=calculation_bill(Previous_reading,Current_reading)

# SUMMARY DISPLAY
print("customer name:   ",customer)
print("your meter number is:  ",meter_number)
print("your previous meter reading:   ",Previous_reading)
print("your current meter reading:   ",Current_reading)
print("unit used:   ",used_units)
print(f"TOTAL BILLS:  ${total_bills}") 
print("===============================")
print("THANK YOU FOR USEING MY WATER BILLING SYSTEM")
print("YOUR ALWAYS WELCOMED AGAIN")
