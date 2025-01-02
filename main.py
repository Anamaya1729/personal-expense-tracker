from datetime import datetime
import argparse
import numpy as np
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.cluster.util import cosine_distance
from nltk.tokenize import sent_tokenize


def add_expense() -> None:
    try:
        expense = input("Enter the expense detail: ")
        amount = float(input("Enter the amount: "))
        with open("expenses.txt", "a") as file:
            file.write(f"{datetime.now().strftime('%d-%b-%Y %H:%M:%S')}: {expense} - Rs. {amount}\n")
        print("Expense added successfully!")
    except ValueError or TypeError:
        print("Invalid input! Please try again.")

    except Exception as e:
        print(f"An error occurred: {e}")


def view_expenses() -> None:
    with open("expenses.txt", "r") as file:
        expenses = file.readlines()
    print("\n--- Expenses List ---")
    for expense in enumerate(expenses, 1):
        print(f"{expense[0]}. {expense[1]}")
    print("---------------------")
    print("")
        
def monthly_summary() -> None:
    with open("expenses.txt", "r") as file:
        expenses = file.readlines()
    current_month = datetime.now().month
    print(f"--- Monthly Summary for {datetime.now().strftime('%B %Y')} ---")
    total_expenses = 0
    for expense in expenses:
        if str(current_month) in expense:
            total_expenses += float(expense.split("Rs. ")[1])
    print(f"Total expenses for the month: Rs. {total_expenses}")
    print(f"Average expenses per day: Rs. {total_expenses/30}")



def top_expenses() -> None:
    with open("expenses.txt", "r") as file:
        expenses = file.readlines()
    print("--- Top Expenses ---")
    expense_amounts = []
    for expense in expenses:
        expense_amounts.append(float(expense.split("Rs. ")[1]))
    top_5_expenses = np.argsort(expense_amounts)[::-1][:5]
    for i, index in enumerate(top_5_expenses, 1):
        print(f"{i}. {expenses[index]}")
    print("--------------------")

def key_insights() -> None:
    with open("expenses.txt", "r") as file:
        expenses = file.readlines()
    print("--- Key Insights ---")
    expense_details = [expense.split(": ")[1].split(" - Rs. ")[0] for expense in expenses]
    expense_amounts = [float(expense.split("Rs. ")[1]) for expense in expenses]
    print(f"Total number of expenses: {len(expenses)}")
    print(f"Most expensive purchase: {expense_details[np.argmax(expense_amounts)]}")
    print(f"Least expensive purchase: {expense_details[np.argmin(expense_amounts)]}")
    print(f"Total expenses: Rs. {np.sum(expense_amounts)}")
    print("--------------------")

def main() -> None:
    print("Welcome to the personal expense tracker!")
    while True:
        try:
            print("Please select an option from the menu below:")
            print("1. Add expense")
            print("2. View expenses")
            print("3. Monthly summary")
            print("4. Top expenses")
            print("5. Key insights")
            print("6. Exit")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                add_expense()
            elif choice == 2:
                view_expenses()
            elif choice == 3:
                monthly_summary()
            elif choice == 4:
                top_expenses()
            elif choice == 5:
                key_insights()
            elif choice == 6:
                print("Exiting the program...")
                break
            else:
                print("Invalid choice! Please try again.")

        except ValueError or TypeError:
            print("Invalid input! Please try again.")

        except Exception as e:
            print(f"An error occurred: {e}")
            break

if __name__ == "__main__":
    main()