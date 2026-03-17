# репозиторий - это проект, в котором находятся все изменения
# commit - закрепить в истории наши изменения в проекте
# master ветка - это чистовик своего рода, полностью рабочий код
# gitflow - алгоритм работы с гитом

# print("Hello World!")
# print("Goodbye World!")

# merge - слияние источников данных после изменений (в одну кучу) вместе с коммитом
# rebase - подгружать все изменения, но наши изменения будут в самом вверху

# print("Test GitHub")

# Условия
# v1
# n1 = 10
# n2 = 20
# v2

# n1, n2 = 10, 20 # множественное присвоение
# print(n1 > n2)
# print(n1 >= n2)
# print(n1 < n2)
# # бинарные операторы - двойные данные с которыми работает оператор
# print(n1 == n2) #возвращение True если оба операнда равны (одинаковые)
# print(n1 != n2) #возвращение True если оба операнды разные

# print(1 == 1 and 3 == 3) #оператор and возвращает True если оба операнда равны, иначе False
# print(1 == 1 or 2 == 3) #оператор возвращает True если хотя бы один операнд равен True, иначе False

# is_valid = False
# print(is_valid)
# print(not is_valid) #not - оператор инверсия, если значение False станет True и наоборот
# print("hello" in "hello world")

# пример с and
# hours = int(input("Enter hours: "))

#v1
# if hours >= 12:
#     print("PM")
#     print("qwerty")
# else: #else - крайний случай и никогда не пишем условий
#     print("AM")

#v2
# if 12 <= hours < 24:
#     print("PM")
# elif 0 <= hours < 12: #elif - else if промежуток между else и if
#     print("qwerty")
# else:
#     print("Ircorrect hours")

#v1
# if hours >= 12:
#      print("PM")
#      print("qwerty")
# else: #else - крайний случай и никогда не пишем условий
#      print("AM")

# Пользователь вводит три цифры с клавиатуры. Зависимо от выбора пользователя программа выводит на экран максимум
# из трех, минимум из трех или среднее арифметическое трех чисел.

# n1 = int(input("Enter first number: "))
# n2 = int(input("Enter second number: "))
# n3 = int(input("Enter third number: "))
#
# print(f"Your numbers is: Number1 = {n1} Number2 = {n2} Number3 = {n3}")
#
# print("Choose operation")
# print("1. Max number")
# print("2. Min number")
# print("3. Avg number")
#
# choice = int(input("Enter your choice: "))
#
# if choice == 1:
#         print("The maximum number is ", max(n1, n2, n3))
# elif choice == 2:
#         print("The minimum number is ", min(n1, n2, n3))
# elif choice == 3:
#         print("The average number is ", (n1 + n2 + n3) / 3)
# else:
#         print("Invalid choice")

# Пользователь вводит клавиатурой количество метров. В зависимости от выбора пользователя программа переводит
# в метры мили, дюймы или ярды.

# metres = int(input("Enter the number of metres: "))
#
# print("Choose action")
# print("1. Miles")
# print("2. Inch")
# print("3. Yards")
#
# choice = int(input("Enter your choice: "))
#
# if choice == 1:
#     print("Miles = ", metres / 1609.344)
# elif choice == 2:
#     print("Inch = ", metres * 39.37)
# elif choice == 3:
#     print("Yards = ", metres / 0.9144)
# else:
#     print("Invalid choice")