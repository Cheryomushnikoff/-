# Задание 1
# Пользователь вводит с клавиатуры набор чисел. По-
# лученные числа необходимо сохранить в список (тип
# списка нужно выбрать в зависимости от поставленной
# ниже задачи). После чего нужно показать меню, в котором
# предложить пользователю набор пунктов:
# 1. Добавить новое число в список (если такое число су-
# ществует в списке, нужно вывести сообщение поль-
# зователю об этом, без добавления числа).
# 2. Удалить все вхождения числа из списка (пользователь
# вводит с клавиатуры число для удаления)
# 3. Показать содержимое списка (в зависимости от вы-
# бора пользователя список нужно показать с начала
# или с конца)
# 4. Проверить есть ли значение в списке
# 5. Заменить значение в списке (пользователь опреде-
# ляет заменить ли только первое вхождение или все
# вхождения)
# В зависимости от выбора пользователя выполняется
# действие, после чего меню отображается снова.
# import re
#
#
# class Node:
#     def __init__(self, value, next, prev):
#         self.value = value
#         self.next = next
#         self.prev = prev
#
#
# class DoubleLinkedList:
#     def __init__(self):
#         self.head = None
#
#     @property
#     def tail(self):
#         if self.head is None:
#             return None
#         current = self.head
#         while current.next:
#             current = current.next
#         return current
#
#     def append(self, value):
#         node = Node(value, None, None)
#         if self.head is None:
#             self.head = node
#             return
#         current = self.head
#         while current.next is not None:
#             current = current.next
#         current.next = node
#         node.prev = current
#
#     def contains(self, value):
#         if self.head is None:
#             print('Cписок пуст!')
#         current = self.head
#         while current:
#             if current.value == value:
#                 return True
#             current = current.next
#         return False
#
#     def replace(self, old_value, new_value):
#         if self.head is None:
#             print("Список пуст!")
#         current = self.head
#         while current:
#             if current.value == old_value:
#                 current.value = new_value
#                 return
#             current = current.next
#         print('Такое значение не найдено! ')
#
#     def replace_all(self, old_value, new_value, every=True):
#         if self.head is None:
#             print('Список пуст!')
#         n = 0
#         current = self.head
#         while current:
#             if current.value == old_value:
#                 n += 1
#                 current.value = new_value
#                 if not every:
#                     return
#             current = current.next
#         if n == 0:
#             print(f'Значение {old_value} не найдено!')
#             return
#         elif n % 10 in [0, 5, 6, 7, 8, 9] or n in [i for i in range(11, 20)]:
#             word = 'вхождений'
#         elif n % 10 == 1:
#             word = 'вхождение'
#         else:
#             word = 'вхождения'
#         print(f'В списке заменено {n} {word} значения "{old_value} на значение {new_value}"')
#
#
#
#     def count(self, value):
#         result = 0
#         if self.head is None:
#             return result
#         current = self.head
#         while current:
#             if current.value == value:
#                 result += 1
#             current = current.next
#         return result
#
#     def reverse_print(self):
#         if self.head is None:
#             return None
#         result = 'None -> '
#         current = self.tail
#         while current:
#             result += f'{current.value} -> '
#             current = current.prev
#         result += 'None'
#         print('\t', result)
#
#     def remove_all(self, values, every=True):
#         if self.head is None:
#             print("Список пуст!")
#             return
#         n = 0
#         while self.head.value == values:
#             n += 1
#             if self.head.next:
#                 self.head = self.head.next
#                 self.head.prev = None
#                 if not every:
#                     return
#             else:
#                 self.head = None
#                 return
#         current = self.head.next
#         while current:
#             if current.value == values:
#                 n += 1
#                 if current == self.tail:
#                     current.prev.next = None
#                     break
#                 current.prev.next = current.next
#                 current.next.prev = current.prev
#                 if not every:
#                     return
#             current = current.next
#         if n == 0:
#             print(f'Значение {values} не найдено!')
#             return
#         elif n % 10 in [0, 5, 6, 7, 8, 9] or n in [i for i in range(11, 20)]:
#             word = 'вхождений'
#         elif n % 10 == 1:
#             word = 'вхождение'
#         else:
#             word = 'вхождения'
#         print(f'Из списка удалено {n} {word} значения "{values}"')
#
#     def append_new_num(self, value):
#         if not self.head:
#             self.head = Node(value, None, None)
#             return
#         if self.head.value == value:
#             print('Такое значение уже есть в списке, оно добавлено не будет!')
#             return
#         current = self.head
#         while current.next:
#             if current.next.value == value:
#                 print('Такое значение уже есть в списке, оно добавлено не будет!')
#                 return
#             current = current.next
#         current.next = Node(value, None, current)
#
#     def __str__(self):
#         if self.head is None:
#             return None
#         result = 'None -> '
#         current = self.head
#         while current:
#             result += f'{current.value} -> '
#             current = current.next
#         result += 'None'
#         return result
#
#
# helper = """
# Меню:
# 1.Добавить новое число в список.
# 2.Удалить все вхождения числа из списка.
# 3.Показать содержимое списка.
# 4.Проверить есть ли значение в списке.
# 5.Заменить значение в списке.
# 6.Меню
# 7.Выход
# """
#
# while True:
#     numbers = input('Введите числа через пробел или запятую или exit:\n')
#     if numbers == 'exit':
#         print('Выход')
#         break
#     numbers = re.split(r'[ ,;]+', numbers)
#     try:
#         numbers = list(map(int, numbers))
#         break
#     except ValueError:
#         print('Ошибка ввода, повторите снова!')
#         continue
#
# print(helper)
#
# if type(numbers) is list:
#     double_list = DoubleLinkedList()
#     for num in numbers:
#         double_list.append(num)
#     while True:
#         try:
#             answer = int(input("\nВведите пункт меню:\n"))
#             if answer == 1:
#                 new_num = int(input('Введите число, которого нет в списке и которое хотите добавить: '))
#                 double_list.append_new_num(new_num)
#             elif answer == 2:
#                 del_num = int(input('Введите число, которое хотите удалить: '))
#                 double_list.remove_all(del_num)
#             elif answer == 3:
#                 direction = input('В каком направлении отобразить список(п - прямое; о - обратное)?\n')
#                 if direction == 'п':
#                     print('\nCписок в прямом направлении:')
#                     print('\t', double_list)
#                 elif direction == 'о':
#                     print('\nCписок в обратном направлении:')
#                     double_list.reverse_print()
#                 else:
#                     raise ValueError
#             elif answer == 4:
#                 value = int(input('Введите значение, которое хотите проверить: '))
#                 if double_list.contains(value):
#                     print(f'Значение {value} присутствует в списке')
#                 else:
#                     print(f'Значение {value} отсутствует в списке')
#             elif answer == 5:
#                 old_value = int(input('Введите значение, которое хотите заменить: '))
#                 every = int(input('Заменить все вхождения данного значения?(0 - нет; 1 - да)'))
#                 new_value = int(input('Введите значение, на которое хотите заменить: '))
#                 double_list.replace_all(old_value, new_value, every)
#             elif answer == 6:
#                 print(helper)
#             elif answer == 7:
#                 print('\nВыход')
#                 break
#         except ValueError:
#             print('\nОшибка ввода, повторите снова!')
#             continue

# Задание 2
# Реализуйте класс стека для работы со строками (стек
# строк).
# Стек должен иметь фиксированный размер.
# Реализуйте набор операций для работы со стеком:
# ■ помещение строки в стек;
# ■ выталкивание строки из стека;
# ■ подсчет количества строк в стеке;
# ■ проверку пустой ли стек;
# ■ проверку полный ли стек;
# ■ очистку стека;
# ■ получение значения без выталкивания верхней строки
# из стека.
# При старте приложения нужно отобразить меню с
# помощью, которого пользователь может выбрать необ-
# ходимую операцию.

# class Plate:
#     def __init__(self, value, prev, num):
#         self.value = value
#         self.prev = prev
#         self.num = num
#
#
# class Stack:
#     def __init__(self, size):
#         self.top = None
#         self.size = size
#
#     def push(self, value):
#         if self.is_empty():
#             self.top = Plate(value, None, 1)
#             return True
#         if self.is_full():
#             print('Стэк уже заполнен!')
#             return False
#         self.top = Plate(value, self.top, self.top.num + 1)
#         return True
#
#     def is_full(self):
#         return self.top.num == self.size
#
#     def is_empty(self):
#         return self.top is None
#
#     def pop(self):
#         if self.is_empty():
#             print('Стэк пуст!')
#             return None
#         value = self.top.value
#         self.top = self.top.prev
#         return value
#
#     def num_of_elem(self):
#         if self.is_empty():
#             return 0
#         return self.top.num
#
#     def clear(self):
#         self.top = None


# menu = """
# 1. помещение строки в стек;
# 2. выталкивание строки из стека;
# 3. подсчет количества строк в стеке;
# 4. проверку пустой ли стек;
# 5. проверку полный ли стек;
# 6. очистку стека;
# 7. получение значения без выталкивания верхней строки из стека.
# 8. вызов меню
# 9. выход
# """
#
# stack = Stack(7)
# print(menu)
#
# while True:
#     try:
#         answer = int(input('\nВыберите пункт из меню: '))
#         if answer == 1:
#             line = input('\nВведите строку для добавления в стек\n')
#             if stack.push(line):
#                 print(f'\nСтрока "{line}" добавлена в стек')
#         if answer == 2:
#             if value := stack.pop():
#                 print(f'\nИз стека вытолкнули строку "{value}" ')
#         if answer == 3:
#             num = stack.num_of_elem()
#             if num % 10 in [0, *range(5, 10)] or num in list(range(11, 20)):
#                 word = 'строк'
#             elif num % 10 == 1:
#                 word = 'строкa'
#             else:
#                 word = 'строки'
#             print(f'\nВ стеке {num} {word}')
#         if answer == 4:
#             if stack.is_empty():
#                 print('\nСтэк пустой!')
#             else:
#                 print('\nСтэк не пустой!')
#         if answer == 5:
#             if stack.is_full():
#                 print('\nСтэк полный!')
#             else:
#                 print('\nСтэк не полный!')
#         if answer == 6:
#             stack.clear()
#             print('\nСтэк очищен!')
#         if answer == 7:
#             if stack.is_empty():
#                 print('\nСтэк пустой!')
#                 continue
#             print(f'\nВерхняя строка в стеке "{stack.top.value}" ')
#         if answer == 8:
#             print(menu)
#         if answer == 9:
#             print('Выход')
#             break
#     except ValueError:
#         print('\nОшибка ввода, повторите снова!')
#         continue

# Задание 3
# Измените стек из второго задания, таким образом,
# чтобы его размер был нефиксированным.
#
# class Plate:
#     def __init__(self, value, prev, num):
#         self.value = value
#         self.prev = prev
#         self.num = num
#
#
# class Stack:
#     def __init__(self, size):
#         self.top = None
#
#     def push(self, value):
#         if self.is_empty():
#             self.top = Plate(value, None, 1)
#             return
#         self.top = Plate(value, self.top, self.top.num + 1)
#
#     def is_empty(self):
#         return self.top is None
#
#     def pop(self):
#         if self.is_empty():
#             print('Стэк пуст!')
#             return None
#         value = self.top.value
#         self.top = self.top.prev
#         return value
#
#     def num_of_elem(self):
#         if self.is_empty():
#             return 0
#         return self.top.num
#
#     def clear(self):
#         self.top = None