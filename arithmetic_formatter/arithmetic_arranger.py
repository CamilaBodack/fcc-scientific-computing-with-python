problems_list = ["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"]


def arithmetic_arranger(problems_list, result):
    operator_list = split_list(problems_list)
    return operator_list


def split_list(list):
    splitted_list = []
    for item in list:
        item = item.split(" ")
        splitted_list.append(item)
    return splitted_list

print(arithmetic_arranger(problems_list, result=True))