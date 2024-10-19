# number = int(input())

# def EndNumberOne (number_in):
#    number_in = number_in % 10
#    if number_in == 1:
#       return True
#    else:
#       return False

# print(EndNumberOne(number))

# def FileTupe (file_name):
#    if ".gif" in file_name:
#       return True
#    else:
#       return False


# items = [
#    "палатка", "спички", "одеяло", "нож", "зефирки", "крючок", "консервы",
# ]

# index_1 = int(input())
# index_2 = int(input())

# print(items[index_1])
# print(items[index_2])

# fruits = ["яблоко", "груша"]

# fruits_add = ["лимон", "банан", "киви"]
# fruits.extend(fruits_add)

# # Не удаляйте код ниже и не редактируйте его, он нужен для проверки

# for fruit in fruits:
#   print(fruit)


# symbols = ["m", "o", "n"]

# count = 0
# while count < 3:
#    symbols.append(input())
#    count += 1

# # Не удаляйте код ниже, он нужен для проверки

# print("".join(symbols))


# managers = ["Алексей", "Денис", "Юля", "Руслан",  "Алексей", "Денис", "Юля"]

# count = 0
# while count < len(managers):
#    if managers[count] == "Денис":
#       managers[count] = "Татьяна"
#    count += 1

# # Не удаляйте код ниже, он необходим для проверки

# for manager in managers:
#   print(manager)


weekdays = [
"pirmdiena", 
"otrdiena", 
"trešdiena",
"ceturtdiena", 
"piektdiena", 
"sestdiena", 
"svētdiena"]

workdays = []
# i = 0
# while i != len(weekdays):
#    if i < 5:
#       workdays.append(weekdays[i])
#    i += 1

for index in weekdays:
   if index < 5:
      workdays.append(weekdays[index])

# Не удаляйте код ниже, он нужен для проверки

for workday in workdays:
  print(workday)
