from fake_math import divide as fd # Из модуля "fake_math" импорт функции 'divide' и присвоение нового имени 'fd'
from true_math import divide as td # Из модуля "true_math" импорт функции 'divide' и присвоение нового имени 'td'

print(fd(69, 3))
print(fd(3, 0))
print(td(49, 7))
print(td(15, 0))