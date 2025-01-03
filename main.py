from datetime import datetime
import csv
import argparse
import numpy as np
import pandas as pd
import nltk
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.cluster.util import cosine_distance
from nltk.tokenize import sent_tokenize
from scipy.cluster.hierarchy import linkage
from scipy.cluster.hierarchy import dendrogram

nltk.download("stopwords")
nltk.download('punkt_tab')

def add_expense() -> None:
    try:
        expense = input("Enter the expense detail: ")
        amount = float(input("Enter the amount: "))
        date = input("Enter the date in the format (DD/MM/YYYY or press enter for current date): ")
        if date == "":
            date = datetime.now().strftime("%d/%b/%Y")
        else:
            date = datetime.strptime(date, "%d/%m/%Y").strftime("%d/%b/%Y")
        with open("expenses.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([expense, amount, date])
        print("Expense added successfully!")
    except ValueError or TypeError:
        print("Invalid amount! Please try again.")
    except Exception as e:
        print(f"An error occurred: {e}")

def view_expenses() -> None:
    with open("expenses.csv", "r") as file:
        expenses = csv.reader(file)
        print("--- Expenses ---")
        for expense in expenses:
            print(f"{expense[0]} - Rs. {expense[1]} - {expense[2]}")
        print("--------------------")
        
def monthly_summary() -> None:
    expenses = pd.read_csv("expenses.csv", header=None)
    expenses.columns = ["Expense", "Amount", "Date"]
    expenses["Date"] = pd.to_datetime(expenses["Date"], format="%d/%b/%Y")
    expenses["Month"] = expenses["Date"].dt.strftime("%b %Y")
    monthly_summary = expenses.groupby("Month")["Amount"].sum()
    print("--- Monthly Summary ---")
    for month, amount in monthly_summary.items():
        print(f"{month}: Rs. {amount}")
    print(f"Average monthly expenses: Rs. {monthly_summary.mean()}")
    print(f"Most expensive month: {monthly_summary.idxmax()} - Rs. {monthly_summary.max()}")
    print(f"Least expensive month: {monthly_summary.idxmin()} - Rs. {monthly_summary.min()}")
    print("--------------------")
    monthly_summary.plot(kind="bar")
    plt.title("Monthly Expense Summary")
    plt.xlabel("Month")
    plt.ylabel("Amount (Rs.)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def top_expenses() -> None:
    expenses = pd.read_csv("expenses.csv", header=None)
    expenses.columns = ["Expense", "Amount", "Date"]
    top_expenses = expenses.groupby("Expense")["Amount"].sum().sort_values(ascending=False).head(5)
    print("--- Top Expenses ---")
    for expense, amount in top_expenses.items():
        print(f"{expense}: Rs. {amount}")
    print("--------------------")
    top_expenses.plot(kind="pie", autopct="%1.1f%%")
    plt.title("Top Expenses")
    plt.ylabel("")
    plt.tight_layout()
    plt.show()

def key_insights() -> None:
    """ Generate key insights using text summarization to summarize the expenses categories """
    pass


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