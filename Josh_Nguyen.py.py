# Importing libraries

import tkinter as tk
import matplotlib.pyplot as plt

# Defining user expense list


user_expense = []


# Functions

def expense_tracker():
    ex_window = tk.Tk()
    ex_window.title("Expense Tracker")
    ex_window.geometry('700x800')

    # Adding user input to the user_expense list

    def add_expense():

        # Validating user input

        try:
            float(amount.get())
            user_expense.append(catagory_chosen.get())
            user_expense.append(float(amount.get()))
            success_message = tk.Label(ex_window,
                                       text="Expense $" + amount.get() +
                                            " of " + catagory_chosen.get() +
                                            " successfully added").pack()

        # Handling errors

        except ValueError:
            error_message = tk.Label(
                ex_window,
                text="That is not a number please try again").pack()

    # Analysing user input

    def analysis():

        # Check if user has input anything

        if not user_expense:
            error_message = tk.Label(
                ex_window,
                text=
                "You have not entered anything, please enter a number to continue"
            ).pack()

        # If user has entered values, then continues

        else:

            # Defining category lists

            housing_spending = []
            food_spending = []
            utilities_spending = []
            personal_spending = []
            entertainment_spending = []
            others_spending = []

            # Sorting user expenses in to seperated category lists

            for i in range(len(user_expense)):

                # Checking if user expense category matches up with the category of the list

                def sort_expense(reference, spending_list):
                    if user_expense[i] == reference:
                        spending_list.append(user_expense[i + 1])

                # Running the function for each category

                sort_expense("Housing", housing_spending)
                sort_expense("Food", food_spending)
                sort_expense("Utilities", utilities_spending)
                sort_expense("Personal", personal_spending)
                sort_expense("Entertainment", entertainment_spending)
                sort_expense("Others", others_spending)

            # Getting the total expense for each category, this is so that I can make graphs later on

            housing_spending_total = sum(housing_spending)
            food_spending_total = sum(food_spending)
            utilities_spending_total = sum(utilities_spending)
            personal_spending_total = sum(personal_spending)
            entertainment_spending_total = sum(entertainment_spending)
            others_spending_total = sum(others_spending)

            # Defining list for drawing charts

            expense_values = [
                housing_spending_total, food_spending_total,
                utilities_spending_total, personal_spending_total,
                entertainment_spending_total, others_spending_total
            ]

            expense_catagorie = [
                "Housing", "Food", "Utilities", "Personal", "Entertainment",
                "Others"
            ]

            # Making a combined list with the total expense for each category with the name of the category

            combined_list = []

            for i in range(len(expense_values)):
                combined_list.append(expense_values[i])
                combined_list.append(expense_catagorie[i])

            # Finding out and displaying the largest and smallest expense

            spend_most = max(expense_values)
            spend_least = min(expense_values)

            for i in range(len(combined_list)):

                if combined_list[i] == spend_most:
                    label_spacing = tk.Label(
                        ex_window,
                        text="-----------------------------------------").pack(
                    )
                    spend_most_cata = combined_list[i + 1]
                    spend_most = str(spend_most)

                    label_spend_most = tk.Label(
                        ex_window,
                        text="Your biggest expense is $" + spend_most +
                             " on " + spend_most_cata).pack()

                    label_spacing = tk.Label(
                        ex_window,
                        text="-----------------------------------------").pack(
                    )

                if combined_list[i] == spend_least:
                    label_spacing = tk.Label(
                        ex_window,
                        text="-----------------------------------------").pack(
                    )
                    spend_least_cata = combined_list[i + 1]
                    spend_least = str(spend_least)
                    label_spend_least = tk.Label(
                        ex_window,
                        text="Your smallest expense is $" + spend_least +
                             " on " + spend_least_cata).pack()

                    label_spacing = tk.Label(
                        ex_window,
                        text="-----------------------------------------").pack(
                    )

            # Ploting the pie chart

            def pie_chart():
                plt.axis('equal')
                plt.pie(expense_values,
                        labels=expense_catagorie,
                        autopct='%0.1f%%')
                plt.show()

            # Ploting the bar chart

            def bar_chart():
                plt.bar(expense_catagorie, expense_values)
                plt.xlabel("Catagorie")
                plt.ylabel("Amount($)")
                plt.title("Here is your detailed spending for last month")
                plt.show()

            # Evaluating user saving goal program

            def saving_goal():

                # Evaluating how long does it take for user to reach their goals

                def evaluate():
                    try:

                        # Validating user input

                        goal = float(user_goal.get())
                        income = float(user_income.get())

                        # Evaluate their goals

                        user_saving = income - sum(expense_values)
                        if user_saving <= 0:
                            label_broke = tk.Label(
                                sa_window,
                                text=
                                "You are broke, you will never reach your goal. Spend less money",
                                width=50,
                                pady=5).pack()
                        else:
                            saving_time = round((goal / user_saving) + 1)
                            income = str(income)
                            expense = round(sum(expense_values), 2)
                            expense = str(expense)
                            saving_time = str(saving_time)
                            user_time = tk.Label(
                                sa_window,
                                text="With a monthly income of $" + income +
                                     " and monthly "
                                     "expense of $" + expense +
                                     " it will take you " + saving_time +
                                     " months to reach your goal",
                                width=200,
                                pady=5).pack()

                    # Handling error

                    except ValueError:
                        error_message = tk.Label(
                            sa_window,
                            text="That is not a number please try again").pack(
                        )

                # Making a saving goal window

                sa_window = tk.Tk()
                sa_window.title("Saving Goal Evaluator")
                sa_window.geometry('700x800')

                # Ask user for their saving goal

                saving_question = tk.Label(sa_window,
                                           text="What is your saving goal?",
                                           width=50,
                                           pady=5).pack()
                user_goal = tk.Entry(sa_window)
                user_goal.pack()

                # Ask user for their income

                income_question = tk.Label(sa_window,
                                           text="What is your income monthly",
                                           width=50,
                                           pady=5).pack()
                user_income = tk.Entry(sa_window)
                user_income.pack()

                # Evaluate button

                evaluate_button = tk.Button(sa_window,
                                            text="Evaluate",
                                            command=evaluate,
                                            pady=5).pack()

            # Show detailed spending

            bar_chart_button = tk.Button(
                ex_window,
                text="Show me my detailed spending for this month",
                command=bar_chart,
                pady=5).pack()

            # Show fund allocation percentage

            pie_chart_button = tk.Button(ex_window,
                                         text="Show me my fund allocation",
                                         command=pie_chart,
                                         pady=5).pack()

            # Show evaluating saving goal

            saving_button = tk.Button(ex_window,
                                      text="Evaluate my saving goal",
                                      command=saving_goal,
                                      pady=5).pack()

    # Getting user input

    instruction = tk.Label(
        ex_window,
        text="Please enter your monthly expenses below:",
        width=50,
        pady=5).pack()

    amount_question = tk.Label(
        ex_window,
        text="How much did you spend on one category? (Input number only)",

        width=50,
        pady=5).pack()

    amount = tk.Entry(ex_window)
    amount.pack()

    catagory_question = tk.Label(ex_window,
                                 text="What category is it? (Click on the button below to choose "
                                      "category)",
                                 width=50,
                                 pady=5).pack()

    catagory_chosen = tk.StringVar()
    catagory_chosen.set("Housing")
    catagory = tk.OptionMenu(ex_window, catagory_chosen, "Housing", "Food",
                             "Utilities", "Personal", "Entertainment",
                             "Others")
    catagory.pack()

    add_expense_button = tk.Button(ex_window,
                           text="Add expense",
                           command=add_expense,
                           pady=3).pack()

    analysis_button = tk.Button(ex_window,
                             text="Show me the analysis",
                             command=analysis,
                             pady=3).pack()


# The main window

root = tk.Tk()
root.title("Personal expense analysis program")
root.geometry('400x400')

# -----------------------------------------------------------------------------------------------

welcome_message = tk.Label(
    root,
    text="Welcome to my expense tracker program, \n"
         "you can track your expenses and evaluate your saving goal\n ",
    width=50,
    pady=5)
welcome_message.pack()

expense_tracker_button = tk.Button(root,
                                   text="Let's get started",
                                   command=expense_tracker,
                                   pady=3)
expense_tracker_button.pack()

# -----------------------------------------------------------------------------------------------

root.mainloop()
