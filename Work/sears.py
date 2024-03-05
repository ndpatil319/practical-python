# One morning, you go out and place a dollar bill on the sidewalk by the sears tower in Chicago
# Each day therafter, you go out double the number of bills. How long does it take for the stack of bills
# to exceed the height of the tower?

bill_thickness = 0.11 * 0.001 # Dollar Bill thickness in Meters
sears_height = 442 # Sears tower in Chicago height
num_bills = 1 #Initalize bill count
num_days = 1 #Initalize day count

while bill_thickness*num_bills < sears_height: #while dollar bill stack height is less than the sears tower height do the below
    print("Days:", num_days,"No. Bills:", num_bills, "Stack height:", bill_thickness*num_bills) # print the day 1 parameters
    num_days += 1 #increment the day count by 1
    num_bills *= 2 # double the bill count each consecutive day

print("Number of days:", num_days) #print total number of days required
print("Numner of Dollar Bills:", num_bills) # total number of dollar bills required
print("Final Height of the Dollar Bill Stack:", bill_thickness*num_bills) #total stack height achieved




