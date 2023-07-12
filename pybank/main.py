import os
import csv
 # Initialize variables
total_months = 0
net_profit_losses = 0
previous_profit_loss = 0
profit_changes = []
dates = []



budget_data_csv = os.path.join("..", "Resources", "budget_data.csv")

with open(budget_data_csv) as csvfile:

    csv_reader = csv.reader(csvfile, delimiter=',')

    next(csv_reader)

    for row in csv_reader:
        # Extract data from row
        date = row[0]
        profit_loss = int(row[1])

        # Calculate total number of months
        total_months += 1

        # Calculate net total amount of profit/losses
        net_profit_losses += profit_loss

        # Calculate change in profit/losses
        if previous_profit_loss != 0:
            profit_change = profit_loss - previous_profit_loss
            profit_changes.append(profit_change)
            dates.append(date)

        previous_profit_loss = profit_loss

# Calculate average change in profit/losses
if len(profit_changes) > 0:
    average_change = sum(profit_changes) / len(profit_changes)
    
else:
    print("Average Change: Not Applicable")

# Find greatest increase and decrease in profits
greatest_increase = max(profit_changes)
greatest_decrease = min(profit_changes)

# Find corresponding dates for greatest increase and decrease
increase_index = profit_changes.index(greatest_increase)
decrease_index = profit_changes.index(greatest_decrease)
greatest_increase_date = dates[increase_index]
greatest_decrease_date = dates[decrease_index]

#  results
print("Financial Analysis")
print("------------------")
print(f"Total Months: {total_months}")
print(f"Net Total: ${net_profit_losses}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")
