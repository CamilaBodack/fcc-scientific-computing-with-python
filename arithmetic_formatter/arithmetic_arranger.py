
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
    lines = []
    for index, item in enumerate(list):
        major_item = max(item)
        separe_result = "-" * (len(major_item) + 2)
        item.append(separe_result)
        for subitem in range(len(item)):
            if item[1] == "+" or item[1] == "-":
                item[0] =  f"{item[0]:>{len(separe_result)}}"
                item[1] =  f"{item[1]} {item[2]:>{len(separe_result)-2}}"
                separator =  f"{separe_result}"
        lines.append(f"{item[0]}\n{item[1]}\n{separator}")
    return lines


print(arithmetic_arranger(problems_list, result=True))