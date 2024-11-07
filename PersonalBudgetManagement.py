# Objective: Build a personal budget management application. The application will manage budget categories like food, entertainment, utilities, etc., ensuring that budget details memain private and are accessed or modified through public methods.abs

# Task 1

# Define BudgetCategory class
class BudgetCategory:

    # Initialize BudgetCategory class with private attributes
    def __init__(self, name, budget):
        self.__name = name
        self.__allocated_budget = budget
        self.__remaining_budget = budget
        
    
    # Task 2

    # Define getter and setter methods for private attributes
    # Getter and Setter method for name attribute
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    # Getter and Setter method for allocated_budget and remaining_budget attributes
    def get_allocated_budget(self):
        return self.__allocated_budget

    def set_allocated_budget(self, budget):

        # Ensures that budget is not negative
        if budget >= 0:
            self.__allocated_budget = budget

            # Added to keep track of remaining budget
            self.__remaining_budget = budget
        else:

            # Throws an error if budget is negative
            raise ValueError("Allocated budget cannot be negative")

    # Task 3

    # Method to keep track of expenses and update remaining budget
    def add_expense(self, amount):
        if amount < 0:
            # Throws an error if expense amount is negative
            raise ValueError("Expense amount cannot be negative")
        
        if amount > self.__remaining_budget:
            # Throws an error if expense amount exceeds remaining budget
            raise ValueError("Expense amount cannot exceed remaining budget")

        self.__remaining_budget -= amount

    # Task 4

    # Method to display category summary
    def display_category_summary(self):
        return f"Category: {self.__name}, Allocated Budget: {self.__allocated_budget}, Remaining Budget: {self.__remaining_budget}"

food_category = BudgetCategory("Food", 500)
food_category.add_expense(100)
food_category.add_expense(50)
print(food_category.display_category_summary())

rent_category = BudgetCategory("Rent", 3000)
rent_category.add_expense(2000)
print(rent_category.display_category_summary())
