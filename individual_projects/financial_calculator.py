# AC 2nd Financial Calculator


# functions

# starting menu
def starting_menu():

    choice = input("\nEnter the number to select an option\n\n1. Savings Time Calculator\n\n2. Compound Interest Calculator\n\n3. Budget Allocator\n\n4. Sales Price Calculator\n\n5. Tip Calculator\n\n").strip().lower()
    return choice

# save for a goal FIX
def save_goal():
    while True:
        while True:
            goal_amount = input("\nWhat amount are you saving to: ")
            if goal_amount.isdigit() or goal_amount.isdecimal():
                goal_amount = float(goal_amount)
                break
            elif goal_amount.isdigit() or goal_amount.isdecimal() == False:
                print("\nInvalid Choice, Please Retry.")
        while True:
            contributing = input("\nHow often are you contributing?\n\n1. Weekly\n\n2. Monthly\n\n")
            if contributing.isdigit()
                contributing = int(goal_amount)
                break
            elif contributing.isdigit()== False:
                print("\nInvalid Choice, Please Retry.")
        while True:
            amount_contributing = input("\nHow much are you contributing each time: ")
            if amount_contributing.isdigit()
                    amount_contributing = int(goal_amount)
                    break
                elif amount_contributing.isdigit()== False:
                    print("\nInvalid Choice, Please Retry.")

        if contributing == 1:
            time = float(goal_amount / amount_contributing)
            print(f"\nIt will take {time:.0f} weeks to save ${goal_amount:.2f}")
        elif contributing == 2:
            time = float((goal_amount / amount_contributing))
            print(f"\nIt will take {time:.0f} months to save ${goal_amount:.2f}")
        else:
            print("\nInvalid Choice, Please Retry.")
            continue

# compound interest FIX
def compound_interest():
    starting_amount = float(input("\nStarting Amount: "))
    interest_rate = float(input("\nInterest Rate Percent: "))
    interest_rate_percentage = float(interest_rate / 100)
    years = int(input("\nYears Spent Compounding: "))

    
    for year in range(years):
        total_amount = float(starting_amount * interest_rate_percentage) + total_amount

    print(f"\nAt the end of {years} years you will have {total_amount}")

# budget allocator
def budget_allocator():
    amount_categories = input("How many budget categories do you have: ")

    def categories(amount_categories):
        count = 0
        categories_list = []
        for categories in range(amount_categories):
            count +=1
            category = input(f"Category {count}:")
            categories_list.append(category)
        
# sales price
def sales_price():
    original_cost = float(input("\nHow much does the item originally cost: "))
    discount = float(input("\nWhat percent is the discount: "))
    discount = discount / 100
    new_price = (original_cost * discount) - original_cost
    print(f"\nThe item now costs ${abs(new_price):.2f}")

# tip calculator
def tip_calculator():
    bill = input("How much is the bill: ")
    percent = input("What percent of tip are you giving: ")
    percent = percent / 100
    tip = bill * percent
    total_amount = bill + tip
    print(f"The tip amount is ${tip} and your total is ${total_amount}")


# calculator loop
while True:
    choice = starting_menu()

    if choice == "1":
        save_goal()
    elif choice == "2":
        compound_interest()
    elif choice == "3":
        budget_allocator()
    elif choice == "4":
        sales_price()
    elif choice == "5":
        tip_calculator()
    else:
        print("\nInvalid Choice, Please Retry.")
        continue