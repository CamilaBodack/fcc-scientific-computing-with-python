
import re

problems_list = ['3801 - 2', '123 + 49']


def arithmetic_arranger(problems_list, result=False):
    operator_list = split_list(problems_list)
    vertical_align = separe_operators(operator_list)
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

def separe_operators(list):
    line_zero = ""
    line_one = ""
    line_two = ""
    lines = []
    for item in list:
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
    lines.append(f"{line_zero}\n")
    lines.append(f"{line_one}\n")
    lines.append(f"{line_two}\n")
    return lines

def make_max_int(list):
    only_digits = []
    for item in list:
        if not item.endswith(("+","-")):
            only_digits.append(int(item))
    return max(only_digits)
   

print(arithmetic_arranger(problems_list, result=True))