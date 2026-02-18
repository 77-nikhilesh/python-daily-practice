# Student Marks Analysis System
marks = [78, 85, 62, 90, 55, 88, 72]

print("Total Marks:", sum(marks))                 # 530
print("Average Marks:", sum(marks) / len(marks)) # 75.71
print("Highest Marks:", max(marks))               # 90
print("Lowest Marks:", min(marks))                # 55

passed = 0
for m in marks:
    if m >= 60:
        passed += 1
print("Students Passed:", passed)                 # 6


# Shopping Cart Billing System
cart = [499, 1299, 299, 799]

print("\nInitial Cart:", cart)

cart.append(599)     # Add new item
cart.remove(299)     # Remove an item

total_bill = sum(cart)
print("Total Bill:", total_bill)

if total_bill > 2000:
    discount = total_bill * 0.10
    print("Final Bill after Discount:", total_bill - discount)
else:
    print("Final Bill:", total_bill)

print("Most Expensive Item:", max(cart))


# Employee Salary Processing
salaries = [25000, 32000, 18000, 40000, 29000]

print("\nOriginal Salaries:", salaries)

for i in range(len(salaries)):
    if salaries[i] < 25000:
        salaries[i] += 3000  # Salary hike

print("Updated Salaries:", salaries)
print("Highest Salary:", max(salaries))

count = 0
for s in salaries:
    if s > 30000:
        count += 1
print("Employees earning above 30k:", count)


# Attendance Management System
attendance = ["P", "A", "P", "P", "A", "P", "P"]

present = attendance.count("P")
absent = attendance.count("A")

print("\nPresent Days:", present)   # 5
print("Absent Days:", absent)       # 2

attendance_percentage = (present / len(attendance)) * 100
print("Attendance Percentage:", attendance_percentage)

if attendance_percentage >= 75:
    print("Eligible for Exam")
else:
    print("Not Eligible")


# Inventory Management System
inventory = ["Laptop", "Mouse", "Keyboard", "Mouse", "Monitor"]

unique_inventory = []
for item in inventory:
    if item not in unique_inventory:
        unique_inventory.append(item)

print("\nUnique Inventory Items:", unique_inventory)

item_to_check = "Mouse"
if item_to_check in inventory:
    print(item_to_check, "is Available")
else:
    print(item_to_check, "is Out of Stock")

inventory.append("Printer")
inventory.remove("Keyboard")

print("Updated Inventory:", inventory)
print("Total Items:", len(inventory))


# Daily Expense Tracker
expenses = [120, 450, 300, 50, 700]

print("\nTotal Expenses:", sum(expenses))  # 1620
print("Highest Expense:", max(expenses))   # 700
print("Lowest Expense:", min(expenses))    # 50

avg_expense = sum(expenses) / len(expenses)
print("Average Expense:", avg_expense)

high_spending_days = 0
for e in expenses:
    if e > avg_expense:
        high_spending_days += 1
print("High Spending Days:", high_spending_days)
