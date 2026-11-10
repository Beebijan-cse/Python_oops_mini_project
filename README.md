# 🏦 Bank Management System

A beginner-friendly, console-based banking program built with Python. It demonstrates object-oriented programming through savings and current accounts, deposits, withdrawals, and account summaries.

## Features

- Create savings and current accounts
- Deposit and withdraw money
- View one account or all accounts
- Display estimated savings interest at a fixed 5% rate
- Show 0% interest for current accounts
- Validate account details and transaction amounts
- Prevent duplicate account numbers during the current session
- Use `Decimal` for money calculations

## Technologies

- Python 3
- Python standard library: `abc` and `decimal`

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
├── bank_management.py
└── README.md
```

## Requirements

- Python 3
- No external packages

## How to Run

Clone the repository and enter its folder:

```bash
git clone https://github.com/Beebijan-cse/Python_oops_mini_project.git
cd Python_oops_mini_project
```

Run the program:

```bash
python bank_management.py
```

## Application Menu

1. Create Account
2. Deposit Money
3. Withdraw Money
4. Display Account
5. Display All Accounts
6. Exit

## Important Note

This is an educational project, not a real banking system. Account information is stored in memory and is lost when the program exits. The 5% savings interest is a simple example calculation, not a real bank rate.

## Author

**Beebijan**  
[GitHub profile](https://github.com/Beebijan-cse)
