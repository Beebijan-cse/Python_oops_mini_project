# 🏦 Bank Management System

A console-based banking application built with Python. It demonstrates object-oriented programming through savings and current accounts, deposits, withdrawals, and account summaries.

## Features

- Create savings and current accounts
- Deposit and withdraw money
- View one account or all accounts
- Display account interest
- Validate basic user input
- Prevent duplicate account numbers

## Technologies

- Python 3
- Python standard library (`abc`)

## OOP Concepts Demonstrated

| Concept | Example in this project |
|---|---|
| Classes and objects | `Bank`, `BankAccount`, `SavingsAccount`, and `CurrentAccount` |
| Encapsulation | Private `__balance` attribute |
| Inheritance | Savings and current accounts extend `BankAccount` |
| Abstraction | `BankAccount` uses `ABC` and `@abstractmethod` |
| Polymorphism | Account classes implement `calculate_interest()` |
| Method overriding | Account classes override `display_details()` |
| Composition | `Bank` manages account objects |

## Project Structure

```text
Python_oops_mini_project/
├── oops.py
└── README.md
```

## How to Run

Make sure Python 3 is installed. Then run:

```bash
git clone https://github.com/Beebijan-cse/Python_oops_mini_project.git
cd Python_oops_mini_project
python oops.py
```

## Application Menu

1. Create Account
2. Deposit Money
3. Withdraw Money
4. Display Account
5. Display All Accounts
6. Exit

## Note

This is an educational project. Account information is kept in memory and is lost when the program exits. It is not intended for real banking transactions.

## Author

**Beebijan**  
[GitHub profile](https://github.com/Beebijan-cse)
