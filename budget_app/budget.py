class Category:
    def __init__(self, budget: str):
        self.budget = budget
        self.ledger = []
        title_line = f"***********{self.budget}**********".ljust(30, "*")
        print(title_line)
        for item in self.ledger:
            print(f"{item}\n")

    def deposit(self, amount: int, description="") -> list:
        new_deposit = {"amount": amount, "description": description}
        return self.ledger.append(new_deposit)

    def withdraw(self, amount: int, description="") -> bool:
        funds = self.check_funds(amount)
        amount_ledger = self.check_amount_in_ledger()
        new_withdraw = {"amount": ((amount) * -1), "description": description}
        if funds and amount < amount_ledger:
            self.ledger.append(new_withdraw)
            return True
        return False

    def check_amount_in_ledger(self):
        total_amount = 0
        for item in self.ledger:
            for key, value in item.items():
                if key == "amount":
                    total_amount = total_amount + value
        return total_amount

    def get_balance(self):
        return self.check_amount_in_ledger()

    def transfer(self, amount: int, budget_instance):
        funds = self.check_funds(amount)
        actual_balance = self.get_balance()
        if amount > actual_balance:
            return False
        if funds:
            self.ledger.append(
                {"amount": -amount, "description": f"Transfer to {budget_instance.budget}"}
            )
            budget_instance.ledger.append(
                {"amount": amount, "description": f"Transfer from {self.budget}"}
            )
            return True

    def check_funds(self, amount: int):
        balance = self.get_balance()
        if amount > balance:
            return False
        return True


def create_spend_chart(categories):
    pass


food = Category("Food")
entertainment = Category("Entertainment")
food.deposit(900, "deposit")
food.withdraw(45.67, "milk, cereal, eggs, bacon, bread")
print(food.get_balance())
