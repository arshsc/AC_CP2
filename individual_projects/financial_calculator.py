# AC 2nd Financial Calculator


# functions

# starting menu
def starting_menu():

    choice = input("\nEnter the number to select an option\n\n1. Savings Time Calculator\n\n2. Compound Interest Calculator\n\n3. Budget Allocator\n\n4. Sales Price Calculator\n\n5. Tip Calculator\n\n").strip().lower()
    return choice


# save for a goal
def save_goal(goal_amount, contributing, amount_contributing):

    if contributing == 1:
        time = float(goal_amount / amount_contributing)
        print(f"\nIt will take {time:.0f} weeks to save ${goal_amount:.2f}")
        return
    
    elif contributing == 2:
        time = float(goal_amount / amount_contributing)
        print(f"\nIt will take {time:.0f} months to save ${goal_amount:.2f}")
        return


# compound interest
def compound_interest(starting_amount, interest_rate, years):

    interest_rate_percentage = interest_rate / 100
    total_amount = starting_amount

    for year in range(years):
        total_amount = total_amount + (total_amount * interest_rate_percentage)

    print(f"\nAt the end of {years} years you will have ${total_amount:.2f}")
    return


# budget allocator
def budget_allocator(amount_categories, categories_list, income, percents):

    def print_budget():

        for i in range(amount_categories):
            amount = income * (percents[i] / 100)
            print(f"\n{categories_list[i]} is ${amount:.2f}")

    print_budget()
    return


# sales price
def sales_price(original_cost, discount):

    discount_percentage = discount / 100
    new_price = original_cost - (original_cost * discount_percentage)
    print(f"\nThe item now costs ${new_price:.2f}")
    return


# tip calculator
def tip_calculator(bill, percent):

    percent = percent / 100
    tip = bill * percent
    total_amount = bill + tip
    print(f"\nThe tip amount is ${tip:.2f} and your total is ${total_amount:.2f}")
    return


def calculator():

    while True:

        choice = starting_menu().strip().lower()

        if choice == "1":

            while True:
                goal_amount = input("\nWhat amount are you saving to: ")
                if goal_amount.replace(".", "", 1).isdigit():
                    goal_amount = float(goal_amount)
                    break
                print("\nInvalid Choice, Please Retry.")

            while True:
                contributing = input("\nHow often are you contributing?\n\n1. Weekly\n\n2. Monthly\n\n")
                if contributing.isdigit():
                    contributing = int(contributing)
                    if contributing == 1 or contributing == 2:
                        break
                print("\nInvalid Choice, Please Retry.")

            while True:
                amount_contributing = input("\nHow much are you contributing each time: ")
                if amount_contributing.replace(".", "", 1).isdigit():
                    amount_contributing = float(amount_contributing)
                    break
                print("\nInvalid Choice, Please Retry.")

            save_goal(goal_amount, contributing, amount_contributing)

        elif choice == "2":

            while True:
                starting_amount = input("\nStarting Amount: ")
                if starting_amount.replace(".", "", 1).isdigit():
                    starting_amount = float(starting_amount)
                    break
                print("\nInvalid Choice, Please Retry.")

            while True:
                interest_rate = input("\nInterest Rate Percent: ")
                if interest_rate.replace(".", "", 1).isdigit():
                    interest_rate = float(interest_rate)
                    break
                print("\nInvalid Choice, Please Retry.")

            while True:
                years = input("\nYears Spent Compounding: ")
                if years.isdigit():
                    years = int(years)
                    break
                print("\nInvalid Choice, Please Retry.")

            compound_interest(starting_amount, interest_rate, years)

        elif choice == "3":

            while True:
                amount_categories = input("\nHow many budget categories do you have: ")
                if amount_categories.isdigit():
                    amount_categories = int(amount_categories)
                    if amount_categories > 0:
                        break
                print("\nInvalid Choice, Please Retry.")

            categories_list = []

            for categories in range(amount_categories):
                category = input(f"\nCategory {categories+1}: ")
                categories_list.append(category)

            while True:
                income = input("\nWhat is your monthly income: ")
                if income.replace(".", "", 1).isdigit():
                    income = float(income)
                    break
                print("\nInvalid Choice, Please Retry.")

            while True:
                percents = []
                print("\nEnter the percentage for each category (must add up to 100%)")

                for category in categories_list:
                    while True:
                        percent = input(f"\nWhat percent is your {category}: ")
                        if percent.replace(".", "", 1).isdigit():
                            percent = float(percent)
                            if percent >= 0:
                                percents.append(percent)
                                break
                        print("\nInvalid Choice, Please Retry.")

                total_percent = sum(percents)

                if round(total_percent, 2) == 100:
                    break

                print("\nPercentages do not add up to 100%. Please enter all percentages again.")

            budget_allocator(amount_categories, categories_list, income, percents)

        elif choice == "4":

            while True:
                original_cost = input("\nHow much does the item originally cost: ")
                if original_cost.replace(".", "", 1).isdigit():
                    original_cost = float(original_cost)
                    break
                print("\nInvalid Choice, Please Retry.")

            while True:
                discount = input("\nWhat percent is the discount: ")
                if discount.replace(".", "", 1).isdigit():
                    discount = float(discount)
                    if 0 <= discount <= 100:
                        break
                print("\nInvalid Choice, Please Retry.")

            sales_price(original_cost, discount)

        elif choice == "5":

            while True:
                bill = input("\nHow much is the bill: ")
                if bill.replace(".", "", 1).isdigit():
                    bill = float(bill)
                    break
                print("\nInvalid Choice, Please Retry.")

            while True:
                percent = input("\nWhat percent of tip are you giving: ")
                if percent.replace(".", "", 1).isdigit():
                    percent = float(percent)
                    if percent >= 0:
                        break
                print("\nInvalid Choice, Please Retry.")

            tip_calculator(bill, percent)

        else:
            print("\nInvalid Choice, Please Retry.")


calculator()
