import os
import csv

csvpath = os.path.join ("..", "..", "budget_data.csv")

with open(csvpath, newline='') as csvfile:
    financial_data = list(csv.reader(csvfile, delimiter=','))

    total = 0
    row_number = 0
    changes = []
    preivous_profit_loss = 0
    max_change = None
    min_change = None
    max_change_date = None
    min_change_date = None 
    
    for row in financial_data[1:]:
        profit_loss = int(row[1])
        total = total + profit_loss
        if row_number != 0:
            current_change = profit_loss - preivous_profit_loss
            changes.append(current_change)
            if max_change is None or max_change < current_change:
                max_change = current_change
                max_change_date = row[0]
            if min_change is None or min_change > current_change:
                min_change = current_change
                min_change_date = row[0]
        preivous_profit_loss = profit_loss
        row_number = row_number + 1
sum_of_changes = sum(changes)
average_change = sum_of_changes / (row_number - 1)

print("Financial Analysis")
print("---------------------")
print("Total Months: " + str(row_number))
print("Total: $" + str(total))
print("Average Change: $" + str(average_change))
print("Greatest Incrase in Profits: " + max_change_date + " " + "$" + str(max_change ))
print("Greatest Decrase in Profits: " + min_change_date + " " + "$" + str(min_change))