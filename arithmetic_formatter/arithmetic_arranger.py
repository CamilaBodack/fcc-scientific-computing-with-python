
problems_list = ['3801 - 2', '45 + 43']


def arithmetic_arranger(problems_list, result=False):
    operator_list = split_list(problems_list)
    vertical_align = separe_operators(operator_list)
    if len(problems_list) > 5:
        return "Error: Too many problems."
    if has_unexpected_char(operator_list):
        return "Error: Operator must be '+' or '-'."
    final_str = ""
    for item in vertical_align:
        final_str += item
    return final_str


def has_unexpected_char(arrange_list):
    not_allowed_items = []
    for arrange in arrange_list:
        for item in arrange:
            if not (str(item).strip().isdigit() or str(item).strip().startswith(("+", "-"))):
                not_allowed_items.append(item)
    return len(not_allowed_items) > 0
    

def split_list(arrange_list):
    splitted_list = []
    for item in arrange_list:
        item = item.split(" ")
        splitted_list.append(item)
    return splitted_list

def separe_operators(arrange_list):
    line_zero = ""
    line_one = ""
    line_two = ""
    lines = []
    for item in arrange_list:
        major_value = make_max_int(item)
        separe_result = "-" * (len(str(major_value))+2)
        item.append(separe_result)
        for index in range(len(item)):
            if item[1] == "+" or item[1] == "-":
                item[0] =  f"{item[0]:>{len(separe_result)}}"
                item[1] =  f"{item[1]} {item[2]:>{len(separe_result)-2}}"
                separator =  f"{separe_result}"
                line_zero += item[0] + "    "
                line_one += item[1] + "    "
                line_two += separator + "    "
    line_zero = line_zero.rstrip()
    line_one = line_one.rstrip()
    line_two = line_two.rstrip()
    lines.append(f"{line_zero}\n")
    lines.append(f"{line_one}\n")
    lines.append(f"{line_two}")
    return lines

def make_max_int(arrange_list):
    only_digits = []
    for item in arrange_list:
        if item.isdigit():
            only_digits.append(int(item))
    return max(only_digits)
   

arithmetic_arranger(problems_list, result=False)