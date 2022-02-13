
problems_list = ['44 + 815', '909 - 2', '45 + 43', '123 + 49',
          '888 + 40', '653 + 87']


def arithmetic_arranger(problems_list, result=False):
    if len(problems_list) > 5:
        return arrange_too_long()
    operator_list = split_list(problems_list)
    vertical_align = separe_operators(operator_list)
    final_str = ""
    for item in vertical_align:
        final_str += item
    return final_str

def arrange_too_long():
    return "Error: Too many problems."

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
        if not item.endswith(("+","-")):
            only_digits.append(int(item))
    return max(only_digits)
   

print(arithmetic_arranger(problems_list, result=False))