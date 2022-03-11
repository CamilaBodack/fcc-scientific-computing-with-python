class Category:
    def __init__(self, budget: str):
        self.budget = budget
        self.ledger = []


    def __str__(self):
        len_str_budget = len(str(self.budget))
        len_side = (30 - len_str_budget) // 2
        title_line = str("".ljust(len_side, "*") + f"{self.budget}" + "".rjust(len_side, "*")
    ).center(30, "*") + "\n"
        ledger_line = self.output_description() + self.output_mount() + "\n"
        print(ledger_line)
    
    def output_description(self):
        ledger_desc = ""
        for item in self.ledger:
            for key, value in item.items():
                if key == "description":
                    ledger_desc = str(str(value).ljust(23, " ")[:23])
        return ledger_desc

    def output_mount(self):
        ledger_mount = ""
        for item in self.ledger:
            for key, value in item.items():
                if key == "amount":
                    ledger_mount = str(str(value).ljust(7, " ")[:7])
        return ledger_mount



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
                {
                    "amount": -amount,
                    "description": f"Transfer to {budget_instance.budget}",
                }
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
print(food.output_mount())