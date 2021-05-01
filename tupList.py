# Создать список и 5 вложенных кортежей.
myList = ["Janar", "22", (2000, False), (28.04), (bool, "Biskek"), (2021, "Kyrgyzstan", True), ("Bootcamp", "MegaCom", True)]

# Создать Tuple из 3 элементов и вывести каждый из них по индексу.
tuple = ("Janar", 2000, False)
print(tuple[0], "\n", tuple[1], "\n", tuple[2])

# Создать Лист и заполнить его 5 РАЗНЫМИ ТИПАМИ ДАННЫХ.
list = ["Hello, Bro!", 1, True, 25.001, ("ha ha")]

# Создать Лист из 5 разных имён.
# 2.Создать пустую строку и через .join() соеденить пустую строку и все имена в списке.
d = " "
lastList = ["Janarbek", "Baha", "Bektur", "Nurbek", "Baktybek"]
print(d.join(lastList))

# Создать Tuple из 15 различных объектов.
# Разрезать Tuple
# на 5 строк по 3 объекта в строке.
NAMES = ('JACK', 'JIMMY', 'JACKSON', 'JHON', 'JACKSON',
         'JHON',  'JIMMY', 'JACKSON', 'JHON','JACK',
         'JIMMY', 'JACK', 'JACKSON', 'JHON', 'JACKSON',
         'JHON','JACK', 'JIMMY', 'JACK', 'JACKSON', 'JHON',)
print(NAMES[0:3])

# Взять Лист №1 и посчитать сколько раз там встречается имя "Jack".
NAMES = ['JACK', 'JIMMY', 'JACKSON', 'JHON', 'JACKSON',
         'JHON',  'JIMMY', 'JACKSON', 'JHON','JACK',
         'JIMMY', 'JACK', 'JACKSON', 'JHON', 'JACKSON',
         'JHON','JACK', 'JIMMY', 'JACK', 'JACKSON', 'JHON',]
print(NAMES.count('JACK'))

# Удалить из Листа №1 все чётные индексы до 10.
counter = 0
while counter != 5:
    if counter % 2 == 0:
        print(NAMES.pop(counter))
    if counter % 2 == 1:
        print(NAMES.pop(counter))
    counter += 1
print(NAMES)


# Создать пустой лист.
# Добавить в него сначала Ваше Имя, Год Рождения, любимый Язык Программирования.
imena = []
imena.insert(0, 'Janarbek')
print(imena)
imena.insert(1, 2001)
print(imena)
imena.insert(2, 'Python')
print(imena)

