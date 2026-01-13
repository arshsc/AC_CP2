# AC 2nd Financial Calculator


# functions

# starting menu
def starting_menu():

    choice = input("\nEnter the number to select an option\n\n1. Savings Time Calculator\n\n2. Compound Interest Calculator\n\n3. Budget Allocator\n\n4. Sales Price Calculator\n\n5. Tip Calculator\n\n").strip().lower() # input to see what the user wants to do
    return choice # return the input


# save for a goal
def save_goal(goal_amount, contributing, amount_contributing):

    if contributing == 1: # if they entered 1, which is weekly
        time = float(goal_amount / amount_contributing) # math
        print(f"\nIt will take {time:.0f} weeks to save ${goal_amount:.2f}") # output for weeks
        return
    
    elif contributing == 2: # if they entered 2, which is monthly
        time = float(goal_amount / amount_contributing) # math
        print(f"\nIt will take {time:.0f} months to save ${goal_amount:.2f}") # output for months
        return


# compound interest
def compound_interest(starting_amount, interest_rate, years):

    interest_rate_percentage = interest_rate / 100 # make the whole interest rate number into a decimal, aka a percentage
    total_amount = starting_amount # set total amount to starting amount for math later

    for year in range(years): # loop to do the equation for how many years
        total_amount = total_amount + (total_amount * interest_rate_percentage) # math

    print(f"\nAt the end of {years} years you will have ${total_amount:.2f}") # output to show how much they will have at the end
    return


# budget allocator
def budget_allocator(amount_categories, categories_list, income, percents):

    def print_budget():  # inner function

        for i in range(amount_categories): # loops for how many categories were entered
            amount = income * (percents[i] / 100) # math
            print(f"\n{categories_list[i]} is ${amount:.2f}") # shows how much each category is

    print_budget() # print the innter function

    return



# sales price
def sales_price(original_cost, discount):

    discount_percentage = discount / 100 # makes the whole number into a decimal, aka a percentage
    new_price = original_cost - (original_cost * discount_percentage) # math
    print(f"\nThe item now costs ${new_price:.2f}") # output the new price
    return


# tip calculator
def tip_calculator(bill, percent):
    percent = percent / 100 # makes the whole number into a decimal, aka a percentage
    tip = bill * percent # math
    total_amount = bill + tip # adds the tip onto the total amount
    print(f"\nThe tip amount is ${tip:.2f} and your total is ${total_amount:.2f}") # outputs the tip and the totla amount
    return



# calculator loop
while True:

    choice = starting_menu().strip().lower() # user input

    if choice == "1": # save for a goal

        while True:
            goal_amount = input("\nWhat amount are you saving to: ") # ask how much they are saving up to

            if goal_amount.replace(".", "", 1).isdigit(): # make sure it is a valid input
                goal_amount = float(goal_amount) # change into a float
                break # break out the loop because it is valid
            print("\nInvalid Choice, Please Retry.") # if it is not a valid input, it retries because it is in a loop

        while True:
            contributing = input("\nHow often are you contributing?\n\n1. Weekly\n\n2. Monthly\n\n") # ask how often they are contributing
            if contributing.isdigit(): # make sure it is a valid input
                contributing = int(contributing) # change into an int
                if contributing == 1 or contributing == 2:  # make sure it is a valid input
                    break # break out the loop because it is valid
            print("\nInvalid Choice, Please Retry.") # if it is not a valid input

        while True:
            amount_contributing = input("\nHow much are you contributing each time: ") # ask how much they are contributing
            if amount_contributing.replace(".", "", 1).isdigit(): # make sure it is a valid input
                amount_contributing = float(amount_contributing) # change into a float
                break # break out the loop because it is valid
            print("\nInvalid Choice, Please Retry.") # if it is not a valid input

        save_goal(goal_amount, contributing, amount_contributing) # do the math and output in the function

    elif choice == "2": # compound interest

        while True:
            starting_amount = input("\nStarting Amount: ") # how much they are starting with
            if starting_amount.replace(".", "", 1).isdigit(): # make sure it is a valid input
                starting_amount = float(starting_amount) # change into a float
                break # break out the loop because it is valid
            print("\nInvalid Choice, Please Retry.") # if it is not a valid input

        while True:
            interest_rate = input("\nInterest Rate Percent: ") # what the interest rate percent is
            if interest_rate.replace(".", "", 1).isdigit(): # make sure it is a valid input
                interest_rate = float(interest_rate) # turn it into a float
                break # break out the loop because it is valid
            print("\nInvalid Choice, Please Retry.") # if it is not a valid input

        while True:
            years = input("\nYears Spent Compounding: ") # ask how many years spent compounding
            if years.isdigit(): # make sure it is a valid input
                years = int(years) # turn into int
                break # break out the loop because it is valid
            print("\nInvalid Choice, Please Retry.") # if it is not a valid input

        compound_interest(starting_amount, interest_rate, years) # do the math and output in the function

    elif choice == "3": # budget allocator

        while True:
            amount_categories = input("\nHow many budget categories do you have: ") # ask how many categories they have
            if amount_categories.isdigit(): # make sure it is a valid input
                amount_categories = int(amount_categories) # turn into int
                if amount_categories > 0: # make sure it is a valid input
                    break # break out the loop because it is valid
            print("\nInvalid Choice, Please Retry.")  # if it is not a valid input

        categories_list = [] # define a categories list

        for categories in range(amount_categories): # loop to happen for every category
            category = input(f"\nCategory {categories+1}: ") # ask the name for each category
            categories_list.append(category) # add each category to the list

        while True:
            income = input("\nWhat is your monthly income: ") # ask the monthly income
            if income.replace(".", "", 1).isdigit(): # make sure it is a valid input
                income = float(income) # turn into float
                break # break out the loop because it is valid
            print("\nInvalid Choice, Please Retry.") # if it is not a valid input

        while True:
            percents = [] # define a percents list
            print("\nEnter the percentage for each category (must add up to 100%)") # ask for each percent and say it must add up to 100%

            for category in categories_list: # happen for every category

                while True:
                    percent = input(f"\nWhat percent is your {category}: ") # ask what percent this category is
                    if percent.replace(".", "", 1).isdigit(): # make sure it is a valid input
                        percent = float(percent) # turn into float

                        if percent >= 0: # make sure it is valid
                            percents.append(percent) # add it to the percent list
                            break # break out the loop because it is valid

                    print("\nInvalid Choice, Please Retry.") # if it is not a valid input

            total_percent = sum(percents) # add all the percents up

            if round(total_percent, 2) == 100: # make sure it equals 100
                break # break out the loop because it is valid

            print("\nPercentages do not add up to 100%. Please enter all percentages again.") # if they do not add up to 100

        budget_allocator(amount_categories, categories_list, income, percents) # do the math and outputs

    elif choice == "4": # sales price

        while True:
            original_cost = input("\nHow much does the item originally cost: ") # ask how much the oriignal cost is

            if original_cost.replace(".", "", 1).isdigit(): # make sure it is a valid input
                original_cost = float(original_cost) # turn into float
                break # break out the loop because it is valid

            print("\nInvalid Choice, Please Retry.") # if it is not a valid input

        while True:
            discount = input("\nWhat percent is the discount: ") # ask how much the discount percent is

            if discount.replace(".", "", 1).isdigit(): # make sure it is a valid input
                discount = float(discount) # turn into float

                if 0 <= discount <= 100: # make sure it is a valid input
                    break # break out the loop because it is valid

            print("\nInvalid Choice, Please Retry.") # if it is not a valid input

        sales_price(original_cost, discount) # do the math and outputs

    elif choice == "5": # tip calculator

        while True:
            bill = input("\nHow much is the bill: ") # ask how much the bill is

            if bill.replace(".", "", 1).isdigit(): # make sure it is a valid input
                bill = float(bill) # turn into float
                break # break out the loop because it is valid

            print("\nInvalid Choice, Please Retry.") # if it is not a valid input

        while True:
            percent = input("\nWhat percent of tip are you giving: ") # ask how much the percent of tip you are giving

            if percent.replace(".", "", 1).isdigit(): # make sure it is a valid input
                percent = float(percent) # turn into float

                if percent >= 0: # make sure it is a valid input
                    break # break out the loop because it is valid

            print("\nInvalid Choice, Please Retry.") # if it is not a valid input

        tip_calculator(bill, percent) # do the math and outputs

    else:
        print("\nInvalid Choice, Please Retry.") # if it is not a valid input