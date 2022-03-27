from re import A


class Category:
    def __init__(self, budget: str):
        self.budget = budget
        self.ledger = []

    def __str__(self):
        len_str_budget = len(str(self.budget))
        len_side = (30 - len_str_budget) // 2
        title_line = str(
            "".ljust(len_side, "*") + f"{self.budget}" + "".rjust(len_side, "*")
        ).center(30, "*")
        ledger_lines = ""
        for index in range(len(self.ledger)):
            ledger_lines = ledger_lines + (
                str(self.output_description(index) + self.output_amount(index)) + "\n"
            )
        total_line = f"Total: {self.check_amount_in_ledger()}"
        return f"{title_line}\n{ledger_lines}{total_line}"

    def output_description(self, index: int) -> str:
        ledger_item = self.ledger[index].items()
        ledger_description = dict(ledger_item)["description"]
        return ledger_description.ljust(23, " ")[:23]

    def output_amount(self, index: int) -> str:
        ledger_item = self.ledger[index].items()
        ledger_amount = float(dict(ledger_item)["amount"])
        ledger_amount = "{:.2f}".format((ledger_amount)).rjust(7, " ")
        return ledger_amount

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

    def check_amount_in_ledger(self) -> int:
        total_amount = 0
        for item in self.ledger:
            amount = dict(item)["amount"]
            total_amount = total_amount + amount
        return total_amount

    def get_balance(self) -> callable:
        return self.check_amount_in_ledger()

    def transfer(self, amount: int, budget_instance: object) -> bool:
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

    def check_funds(self, amount: int) -> bool:
        balance = self.get_balance()
        if amount > balance:
            return False
        return True


def create_spend_chart(categories: list) -> str:
    all_withdraws_by_category = []
    for item in categories:
        for category_data in item.ledger:
            if category_data["amount"] < 0:
                all_withdraws_by_category.append(
                    {"category": item.budget, "total": category_data["amount"]}
                )

    percent_by_category_formatter = f"Percentage spent by category\n"
    matrix = matrix_line_and_column(all_withdraws_by_category)

    # print("Percentage spent by category\n100|          \n 90|          \n 80|          \n 70|    o     \n 60|    o     \n 50|    o     \n 40|    o     \n 30|    o     \n 20|    o  o  \n 10|    o  o  \n  0| o  o  o  \n    ----------\n     B  F  E  \n     u  o  n  \n     s  o  t  \n     i  d  e  \n     n     r  \n     e     t  \n     s     a  \n     s     i  \n           n  \n           m  \n           e  \n           n  \n           t  ")


def total_withdraw(all_withdraws_by_category: list) -> int:
    total_withdraw = 0
    for category_data in all_withdraws_by_category:
        total_withdraw = total_withdraw + category_data["total"]
    total_withdraw = total_withdraw * (-1)
    return total_withdraw


def total_by_category(all_withdraws_by_category: list):
    total = total_withdraw(all_withdraws_by_category)
    category_total = []
    for category_data in all_withdraws_by_category:
        category_percent = round(((category_data["total"] * (-1)) * 10) / total) * 10
        category_total.append(
            {"category": category_data["category"], "percent": category_percent}
        )
    return category_total


def create_matrix(all_withdraws_by_category: list) -> list:
    max_category_str_length = 0
    len_category_objects = len(all_withdraws_by_category)
    for item in all_withdraws_by_category:
        if len(item["category"]) > max_category_str_length:
            max_category_str_length = len(item["category"])
    matrix_lines = (
        12 + max_category_str_length
    )  # 12 is the range of 0 - 10 plus sepator line
    matrix_columns = 3 + (
        len_category_objects * 3
    )  #  3 is the len of percent number plus | plus extra final space
    matrix = [["X" for column in range(matrix_columns)] for line in range(matrix_lines)]
    return matrix


def set_default_column_data(all_withdraws_by_category):
    matrix = create_matrix(all_withdraws_by_category)


food = Category("Food")
entertainment = Category("Entertainment")
business = Category("Business")
food.deposit(900, "deposit")
entertainment.deposit(900, "deposit")
business.deposit(900, "deposit")
food.withdraw(105.55)
entertainment.withdraw(33.40)
business.withdraw(10.99)
create_spend_chart([business, food, entertainment])
