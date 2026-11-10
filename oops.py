from abc import ABC, abstractmethod
from decimal import Decimal, InvalidOperation


SAVINGS_INTEREST_RATE = Decimal("0.05")


class BankAccount(ABC):
    """Base class for bank accounts."""

    def __init__(self, name, account_number, balance):
        if not balance.is_finite() or balance < 0:
            raise ValueError("Balance must be finite and non-negative.")

        self.name = name
        self.account_number = account_number
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if not amount.is_finite() or amount <= 0:
            print("Enter a finite amount greater than zero.")
            return

        self.__balance += amount
        print("Deposit successful!")

    def withdraw(self, amount):
        if not amount.is_finite() or amount <= 0:
            print("Enter a finite amount greater than zero.")
        elif amount > self.__balance:
            print("Insufficient balance!")
        else:
            self.__balance -= amount
            print("Withdrawal successful!")

    @abstractmethod
    def calculate_interest(self):
        """Return the interest for this account."""
        pass

    def display_details(self):
        print("\nAccount Holder:", self.name)
        print("Account Number:", self.account_number)
        print(f"Balance: Rs. {self.__balance:.2f}")


class SavingsAccount(BankAccount):
    """Bank account that earns interest at a fixed example rate."""

    def calculate_interest(self):
        return self.get_balance() * SAVINGS_INTEREST_RATE

    def display_details(self):
        print("\n--- Savings Account ---")
        super().display_details()
        print(f"Estimated Interest: Rs. {self.calculate_interest():.2f}")


class CurrentAccount(BankAccount):
    """Bank account with no interest in this example program."""

    def calculate_interest(self):
        return Decimal("0.00")

    def display_details(self):
        print("\n--- Current Account ---")
        super().display_details()
        print(f"Interest: Rs. {self.calculate_interest():.2f}")


class Bank:
    """Manage accounts for the current program session."""

    def __init__(self):
        self.accounts = []

    def create_account(self):
        name = input("Enter account holder name: ").strip()
        if not name:
            print("Name cannot be empty!")
            return

        account_number = input("Enter account number: ").strip()
        if not account_number:
            print("Account number cannot be empty!")
            return

        for account in self.accounts:
            if account.account_number == account_number:
                print("Account number already exists!")
                return

        try:
            balance = Decimal(input("Enter initial balance: ").strip())
        except InvalidOperation:
            print("Please enter a valid balance!")
            return

        if not balance.is_finite() or balance < 0:
            print("Balance must be finite and non-negative!")
            return

        print("\n1. Savings Account")
        print("2. Current Account")
        choice = input("Choose account type: ").strip()

        if choice == "1":
            account = SavingsAccount(name, account_number, balance)
        elif choice == "2":
            account = CurrentAccount(name, account_number, balance)
        else:
            print("Invalid account type!")
            return

        self.accounts.append(account)
        print("\nAccount created successfully!")

    def find_account(self):
        account_number = input("Enter account number: ").strip()

        for account in self.accounts:
            if account.account_number == account_number:
                return account

        print("Account not found!")
        return None

    def deposit_money(self):
        account = self.find_account()
        if account is None:
            return

        try:
            amount = Decimal(input("Enter deposit amount: ").strip())
        except InvalidOperation:
            print("Please enter a valid amount!")
            return

        account.deposit(amount)

    def withdraw_money(self):
        account = self.find_account()
        if account is None:
            return

        try:
            amount = Decimal(input("Enter withdrawal amount: ").strip())
        except InvalidOperation:
            print("Please enter a valid amount!")
            return

        account.withdraw(amount)

    def display_account(self):
        account = self.find_account()
        if account is not None:
            account.display_details()

    def display_all_accounts(self):
        if not self.accounts:
            print("No accounts available!")
            return

        for account in self.accounts:
            account.display_details()


def main():
    bank = Bank()

    while True:
        print("\n================================")
        print("       BANK MANAGEMENT SYSTEM")
        print("================================")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Display Account")
        print("5. Display All Accounts")
        print("6. Exit")
        print("================================")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            bank.create_account()
        elif choice == "2":
            bank.deposit_money()
        elif choice == "3":
            bank.withdraw_money()
        elif choice == "4":
            bank.display_account()
        elif choice == "5":
            bank.display_all_accounts()
        elif choice == "6":
            print("Thank you for using Bank Management System!")
            break
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
