table = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]

menu = [["Breakfast", "1", "All Day(large)", 5.50],
        ["Breakfast", "2", "All Day(small)", 3.50],
        ["Mains    ", "3", "Hot Dog       ", 3.00],
        ["Mains    ", "4", "Burger        ", 4.00],
        ["Mains    ", "5", "Cheese Burger ", 4.25],
        ["Mains    ", "6", "Chicken Goujons", 3.50],
        ["Extras   ", "7", "Fries          ", 1.75],
        ["Extras   ", "8", "Salad          ", 2.20],
        ["Drinks   ", "9", "Milkshake      ", 2.20],
        ["Drinks   ", "10", "Soft Drinks   ", 1.30],
        ["Drinks   ", "11", "Still Water   ", 0.90],
        ["Drinks   ", "12", "Sparkling water", 0.90]]

ask = "Yes"
total0 = 0
total1 = 0
# first value is menu number and second value is quantity
ordered_items=[["3","1"], ["7","2"]]

while ask != "No":
    num = input("Enter number of the item you would like to order: ")
    for i in menu:
        if i[1] == num:
            print("You have selected: ", i[2])
            quantity = int(input("Enter the quantity you would like:  "))
            total0 = quantity * i[3]
            total1 = total1 + total0
            ask = input("Would you like anything else? Enter 'Yes' or 'No': ")

print("The total is £",total1,)

print("Select a table")

intable = input("Enter your table number: ")
if intable in table:
    print(
        "You have selected table no. ",
        intable,
    )
elif intable not in table:
    print("We don't have that many tables!Please re-enter your table number")

#order details for printing
print("Table",intable,)
print("Order:",quantity,"x",i,)

for item_and_quantity in ordered_items:
    print(item_and_quantity[1],"x Menu Item", item_and_quantity[0],)






