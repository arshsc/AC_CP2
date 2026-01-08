# AC 2nd Financial Calculator


# functions
# starting menu
def starting_menu():
    choice = input("Enter the number to select an option\n\n1. Savings Time Calculator\n\n2. Compound Interest Calculator\n\n3. Budget Allocator\n\n4. Sales Price Calculator\n\n5. Tip Calculator\n\n").strip().lower()
    return choice

# Save for a goal
def save_goal():
    goal_amount = input("\n\nWhat amount are you saving to: ").strip().lower()
    contributing = input("How often are you contributing?\n\n1. Weekly\n\n2. Monthly\n\n").strip().lower()
    amount_contributing = input("\n\nHow much are you contributing each time: ").strip().lower()

    if contributing == 1:
        time = goal_amount / amount_contributing
        print(f"It will take {time} months to save${goal_amount}")

# compount interest
def compound_interest():
    starting_amount = input("Starting Amount: ")
    interest_rate = input("Interest Rate Percent: ")
    interest_rate_percentage = interest_rate / 100
    years = input("Years Spent Compounding: ")

    while years <= 0:
        total_amount = starting_amount * interest_rate_percentage
        print(f"At the end of {years} years you will have {total_amount}")

# budget allocator
def budget_allocator():
# sakes price

# tip calculator


choice = starting_menu()
if choice == "1":
    save_goal()