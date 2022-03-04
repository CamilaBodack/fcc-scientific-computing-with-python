class Category:
    def __init__(self, budget: str):
        self.budget = budget
        self.ledger = []

    def deposit(self, deposit_amount: int, description: str) -> list:
        new_desc = self.set_default_str(description)
        new_deposit = {"amount": deposit_amount, "description": new_desc}
        return self.ledger.append(new_deposit)

    def set_default_str(self, info: str) -> str:
        if not info:
            return ""
        return info

    def withdraw(self, withdraw_amount: int, description: str) -> bool:
        new_desc = self.set_default_str(description)
        amount_ledger = self.check_amount_in_ledger()
        new_withdraw = {"amount": -withdraw_amount, "description": new_desc}
        if amount_ledger > 0:
            self.ledger.append(new_withdraw)
            return True
        return False

    def check_amount_in_ledger(self):
        total_amount = 0
        for key, value in self.ledger:
            if key == "amount":
                total_amount = total_amount + value
        return total_amount


    def has_amount(self, total_amount: int, withdraw_amount: int):
        return (total_amount - withdraw_amount) > 0






def create_spend_chart(categories):
    pass