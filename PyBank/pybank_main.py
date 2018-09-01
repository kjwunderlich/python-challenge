import os
import csv

csvpath = "python-challenge", "PyBank", "budget_data.csv"

with open(csvpath, newline='') as csvfile:
    financial_data = csv.reader(csvfile, delimiter=',')
    next(financial_data)

    list_of_values = 0
    total = 0
    row_number = 0
    changes = []
    
    for row in financial_data:
        profit_loss = int(row[1])
        print(profit_loss)
        
        if row_number != 1:
            list_of_values = int(row[1])
            print(list_of_values)
        total = total + profit_loss
        change =  next(list_of_values) - profit_loss
        changes.append(change)
        row_number = row_number + 1
        sum_of_changes = sum(changes)
        average_change = sum_of_changes / row_number
    print(changes)    
    
#     Row = next (csvreader)             #in row 1
# Total = row[1]
# Profit_loss = row[1]
# For row in csvreader:                   #now on row 2
#     Change = row[1] – profit_loss
#     Profit_loss = row[1]
#        total = total + row[1]
    
    
    # for value in changes:
    #     if value + 1 > value:
    #         greatest_increase = value + 1
    #     if value + 1 < value:
    #         greatest_decrease = value + 1

    print(row_number)
    print(total)
    print(average_change)
    #print(greatest_increase)
    #print(greatest_decrease)

    # print("Financial Analysis")
    # print("---------------------")
    # print("Total Months: " + str(row_number))
    # print("Total: $" + str(total))
    # print("Average Change: $" + str(average_change))
    # print("Greatest Incrase in Profits: $" + )
    # print("Greatest Decrase in Profits: $" + )