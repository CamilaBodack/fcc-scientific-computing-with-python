class Category:
    def __init__(self, budget: str):
        self.budget = budget
        self.ledger = []

    def deposit(self, amount: int, description="") -> list:
        new_desc = description
        new_deposit = {"amount": amount, "description": new_desc}
        return self.ledger.append(new_deposit)

    def withdraw(self, amount: int, description="") -> bool:
        new_desc = description
        amount_ledger = self.check_amount_in_ledger()
        new_withdraw = {"amount": ((amount) * -1), "description": new_desc}
        if amount < amount_ledger:
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


def create_spend_chart(categories):
    pass


food = Category("Food")
food.deposit(900, "deposit")
food.withdraw(45.67, "milk, cereal, eggs, bacon, bread")
print(food.get_balance())
