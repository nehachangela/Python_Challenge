# This will allow us to creat file paths across 
import os
# Module for reading CSV files
import csv

# Set path for file
csvpath = os.path.join("Resources","budget_data.csv")

print("Financial Analysis")
print("----------------------------------------")

# Open the CSV 
with open(csvpath) as budget_data:
    csvreader = csv.reader(budget_data, delimiter = ",")
    #next()	Returns the next item in an iterable
    csv_header = next(csvreader)

    # declaring Variable that need to be calculated
    Months = 0
    Total = 0
    previous_value = 0
    Total_change = 0
    current_change = 0
    count = 0
    greatest_increase = 0
    greatest_decrease = 0
    
    for row in csvreader:
        #Adding up months
        Months = Months + 1
        #Total profit/losses
        Total = Total + int(row[1])
        
        #Count is used here to set first month change to zero due to no previous month available
        count = count + 1
        current_value = int(row[1])

        #Calculate current profit/losses change    
        if (count>1):
            current_change = current_value - previous_value
        #Calculating greatest increase in current change
        if (current_change > greatest_increase):
            greatest_increase = current_change
            # Month with greatest increase
            greatest_increase_month = row[0]
        # Calculating greatest decrease in current change
        if (current_change < greatest_decrease):
            greatest_decrease = current_change
            # Month with greatest decrease
            greatest_decrease_month = row[0]

        #Resetting previous value to calculate next row
        previous_value = current_value
        #Calculating total profit change
        Total_change = Total_change + current_change
    
    Average_change = Total_change/(Months-1)

    print("Total Months: " + str(Months))
    print("Total Profit: " + str(Total))
    print(f"Average Change:  {Average_change:.2f}")
    print("Greatest Increase: " + str(greatest_increase_month) + "  $ " + str(greatest_increase))
    print("Greatest Decrease: " + str(greatest_decrease_month) + "  $ " + str(greatest_decrease))

    # creating text file in the same folder as excel budget_data
    output = os.path.join("analysis", "budget_data_Analysis.txt")
    with open(output, 'w') as datafile:
        newline = csv.writer(datafile)
        newline.writerow(["Financial Analysis"])
        newline.writerow(["------------------------------"])
        newline.writerow(["Total Months: " + str(Months)])
        newline.writerow([f"Average Change:  {Average_change:.2f}"])
        newline.writerow(["Greatest Increase: " + str(greatest_increase_month) + " $" + str(greatest_increase)])
        newline.writerow(["Greatest Decrease: " + str(greatest_decrease_month) + " $" + str(greatest_decrease)])
