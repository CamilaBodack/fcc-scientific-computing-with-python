
problems_list = ["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"]


def arithmetic_arranger(problems_list, result):
    operator_list = split_list(problems_list)
    vertical_align = separe_operators(operator_list)
    for item in vertical_align:
        print(item)


def split_list(list):
    splitted_list = []
    for item in list:
        item = item.split(" ")
        splitted_list.append(item)
    return splitted_list

def separe_operators(list):
    vertical_arrange = []
    for item in list:
        major_item = max(item)
        separe_result = "-" * len(major_item)
        item.append(separe_result)
        for subitem in item:
            vertical_arrange.append(subitem)
    return vertical_arrange


print(arithmetic_arranger(problems_list, result=True))