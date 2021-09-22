problems_list = ['32 - 698', '1 - 3801', '45 + 43', '123 + 49', '988 + 40']

def arithmetic_arranger(problems_list):
  list_arithmetic_data = problems_list
  arranged_problems = ""
  a = ""
  for item in list_arithmetic_data:
      a = item.replace(" ", "\n")

  arranged_problems = a
  print(arranged_problems)

print(arithmetic_arranger(problems_list))