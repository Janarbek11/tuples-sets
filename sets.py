# Из множества
# № 1 - удалите все числа 7
dates_of_birth = {3, 10, 11, 13, 31, 21, 1, 10, 3, 5, 6, 6}
print(dates_of_birth)
dates_of_birth.remove(6)
print(dates_of_birth)

# Создайте SET состоящий из 3 вложенных SET.
# mySet = set()
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = {'janar', '423', 'haha'}

newset = x.union(y)

print(z)


# Во множестве №3 найдите объекты которых нет во множестве №2
farm1 = {"dog", "cat", "mouse", "sheep"}
farm2 = {"cow", "horse", "donkey", "cat", "dog"}
a = farm2.difference(farm1)
print(a)

# Создайте SET из 5 элементов. Потом добавьте в SET ещё один элемент.
# А затем удалите через .pop() элемент и посмотрите что же вы удалили.

s = {3, 10, 11, 13, 31}
s.add(7)
print(s)
print(s.pop())
print(s)





