problems_list = ['32 - 698', '1 - 3801', '45 + 43', '123 + 49', '988 + 40']

def arithmetic_arranger(problems_list, result):
  list_arithmetic_data = problems_list
  arranged_problems = 0
  for each_arithmetic_operation in list_arithmetic_data:
    each_arithmetic_operation = each_arithmetic_operation.split()
    each_arithmetic_operation.append("-----")
    for each_arithmetic_subitem in each_arithmetic_operation:
      each_arithmetic_subitem = each_arithmetic_subitem.replace(" ", "\n")
      if(result):
        if '+' in each_arithmetic_operation:
          arranged_problems = int(each_arithmetic_operation[0]) + int(each_arithmetic_operation[2])
        if '-' in each_arithmetic_operation:
          arranged_problems = int(each_arithmetic_operation[0]) - int(each_arithmetic_operation[2])
        if '*' in each_arithmetic_operation:
          arranged_problems = int(each_arithmetic_operation[0]) * int(each_arithmetic_operation[2])
        if '/' in each_arithmetic_operation:
          arranged_problems = int(each_arithmetic_operation[0]) / int(each_arithmetic_operation[2])

  print(arranged_problems)

print(arithmetic_arranger(problems_list, result=True))