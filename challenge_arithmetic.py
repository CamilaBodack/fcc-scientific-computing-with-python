problems_list = ['32 - 698', '1 - 3801', '45 + 43', '123 + 49', '988 + 40']

def arithmetic_arranger(problems_list, result):
  list_arithmetic_data = problems_list
  arranged_problems = 0
  for arithmetic_operation in list_arithmetic_data:
    arithmetic_operation = arithmetic_operation.split()
    arithmetic_operation.append("-----")
    for arithmetic_subitem in arithmetic_operation:
      arithmetic_subitem = f"{arithmetic_subitem[0]}{arithmetic_subitem[1]}{arithmetic_subitem[2]}"
      print("--------------------------", arithmetic_subitem)
      if(result):
        if '+' in arithmetic_operation:
          arranged_problems = int(arithmetic_operation[0]) + int(arithmetic_operation[2])
          print(arithmetic_subitem)
          arithmetic_subitem = str( arranged_problems)
        if '-' in arithmetic_operation:
          arranged_problems = int(arithmetic_operation[0]) - int(arithmetic_operation[2])
          arithmetic_subitem = str(arithmetic_subitem) + str(arranged_problems)
          print(arithmetic_subitem)
        if '*' in arithmetic_operation:
          arranged_problems = int(arithmetic_operation[0]) * int(arithmetic_operation[2])
          arithmetic_subitem = str(arithmetic_subitem) + str(arranged_problems)
          print(arithmetic_subitem)
        if '/' in arithmetic_operation:
          arranged_problems = int(arithmetic_operation[0]) / int(arithmetic_operation[2])
          arithmetic_subitem = str(arithmetic_subitem) + str(arranged_problems)
          print(arithmetic_subitem)


print(arithmetic_arranger(problems_list, result=True))