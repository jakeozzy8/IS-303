#create a Python program that analyzes a series of personal finance expenses

small_count = 0
moderate_count = 0
large_count = 0
expenses = []

#ask to enter expense
while True:
    #determine size of expense
    expense_input = float(input("Enter an expense or put 0 to finish: "))
    if expense_input == 0:
        break
    elif expense_input < 0:
        print("Expenses can't be negative.")
    elif expense_input < 25:
        expenses.append(expense_input)
        small_count += 1
    elif expense_input >= 25 and expense_input <= 100:
        expenses.append(expense_input)
        moderate_count += 1
    elif expense_input > 100:
        expenses.append(expense_input)
        large_count += 1

#Find Total expense amount, expense count, and expense average
expense_total = sum(expenses)
expense_count = small_count + moderate_count + large_count
expense_average = expense_total / expense_count

#Print Results
print("Expense Summary")
print("---------------")
print("Number of Expenses: " + str(expense_count))
print(f"Total Expenses:  ${expense_total:,.2f}")
print(f"Average Expense: ${expense_average:,.2f}")
print(f"Highest Expense: ${max(expenses):,.2f}")
print(f"Lowest Expense: ${min(expenses):,.2f}", "\n")

print("Small Expenses: " + str(small_count))
print("Moderate Expenses: " + str(moderate_count))
print("Large Expenses: " + str(large_count))
