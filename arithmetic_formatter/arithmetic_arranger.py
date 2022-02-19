problems_list = ["3 + 855", "3801 - 2", "45 + 43", "123 + 49"]


def arithmetic_arranger(problems_list, result=False):
    if len(problems_list) > 5:
        return "Error: Too many problems."
    if has_only_digits(problems_list):
        return "Error: Numbers must only contain digits."
    if has_extra_digit(problems_list):
        return "Error: Numbers cannot be more than four digits."
    if has_unexpected_operator(problems_list):
        return "Error: Operator must be '+' or '-'."
    operator_list = split_list(problems_list)
    vertical_align = mount_lines(operator_list, result)
    final_str = ""
    for item in vertical_align:
        final_str += item
    return final_str


def split_list(list):
    splitted_list = []
    for item in list:
        item = item.split(" ")
        splitted_list.append(item)
    return splitted_list


def mount_lines(arrange_list, result):
    line_zero = ""
    line_one = ""
    line_two = ""
    line_three = ""
    lines = []
    for item in arrange_list:
        str_to_eval = prepare_eval(item)
        eval_result = str(eval(str_to_eval))
        major_value = make_max_int(item)
        separe_result = "-" * (len(str(major_value)) + 2)
        item.append(separe_result)
        for index in range(len(item)):
            if item[1] == "+" or item[1] == "-":
                item[0] = f"{item[0]:>{len(separe_result)}}"
                item[1] = f"{item[1]} {item[2]:>{len(separe_result)-2}}"
                eval_result = f"{eval_result:>{len(separe_result)}}"
                separator = f"{separe_result}"
                line_zero += item[0] + "    "
                line_one += item[1] + "    "
                line_two += separator + "    "
                line_three += eval_result + "    "
    line_zero = line_zero.rstrip()
    line_one = line_one.rstrip()
    line_two = line_two.rstrip()
    line_three = line_three.rstrip()
    lines.append(f"{line_zero}\n")
    lines.append(f"{line_one}\n")

    if result:
        lines.append(f"{line_two}\n")
        lines.append(f"{line_three}")
    else:
        lines.append(f"{line_two}")
    return lines


def prepare_eval(arrange):
    str_arrange = ""
    for item in arrange:
        str_arrange += item
    return str_arrange


def has_only_digits(list):
    arrange_elements = split_list(list)
    non_digits = []
    for arrange in arrange_elements:
        for index in range(len(arrange)):
            if index == 1:
                continue
            if not (arrange[index].isdigit()):
                non_digits.append(arrange[index])
    return len(non_digits) > 0


def has_extra_digit(list):
    arrange_elements = split_list(list)
    extra_digits_elements = []
    for arrange in arrange_elements:
        for each_element in arrange:
            if len(each_element) > 4:
                extra_digits_elements.append(each_element)
    return len(extra_digits_elements) > 0


def has_unexpected_operator(list):
    arrange = split_list(list)
    not_allowed_items = []
    for arrange_element in arrange:
        for index in range(len(arrange_element)):
            if index != 1:
                continue
            item = arrange_element[index].strip()
            if not (item.isdigit() or item.startswith(("+", "-")) or item == ""):
                not_allowed_items.append(item)
    return len(not_allowed_items) > 0


def make_max_int(arrange_list):
    only_digits = []
    for item in arrange_list:
        if item.isdigit():
            only_digits.append(int(item))
    return max(only_digits)


print(arithmetic_arranger(problems_list, result=True))
