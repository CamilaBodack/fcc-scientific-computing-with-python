from itertools import zip_longest


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

    # Data treatment to create the chart
    fill_matrix = f"Percentage spent by category\n"

    # % by category "o" times
    percent_and_name_dict = total_by_category(all_withdraws_by_category)
    default_colum_data = set_default_column_data(all_withdraws_by_category)

    # Extractor loops
    column_item = []
    for category in percent_and_name_dict:
        for item , default_data in zip_longest(category, default_colum_data):
            if item:
                percent = category["percent"] // 10
                item_percent = set_percent_in_matrix(percent)
                category_name = category["category"]
                column_name = set_category_name_in_matrix(category_name)
                column_item.append(f"{item_percent}{column_name}")
        column_item.append(default_data)

    for item in column_item:
        print(item, sep="\n")

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


def set_default_column_data(all_withdraws_by_category):
    max_category_str_length = 0
    column_zero_spaces = "    "
    for item in all_withdraws_by_category:
        if len(item["category"]) > max_category_str_length:
            max_category_str_length = len(item["category"])
    matrix_column_zero = [
        "100|",
        " 90|",
        " 80|",
        " 70|",
        " 60|",
        " 50|",
        " 40|",
        " 30|",
        " 20|",
        " 10|",
        "  0|",
    ]
    for index in range(max_category_str_length):
        matrix_column_zero.append(column_zero_spaces)
    return matrix_column_zero


def set_percent_in_matrix(percent: int) -> str:
    item_column_percent = []
    for index in range(percent):
        item_column_percent.append(" o ")
    len_column = len(item_column_percent)
    while len_column < 11:
        item_column_percent.insert(0, "   ")
        len_column = len(item_column_percent)
    item_column_percent.append("---")
    return str(item_column_percent)


def set_last_column(all_withdraws_by_category: list):
    last_column = []
    categories = total_by_category(all_withdraws_by_category)
    categories_str = [name["category"] for name in categories]
    max_str_len_category = len(max(categories_str, key=len))
    for index in range(10):
        last_column.append("\n")
    last_column.append("-")
    for index in range(max_str_len_category):
        last_column.append("\n")
    return last_column


def set_category_name_in_matrix(name: str):
    column_name = []
    for letter in name:
        column_name.append(letter)
    return column_name


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
