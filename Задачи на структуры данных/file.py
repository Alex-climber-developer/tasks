def shet_letters(w1,w2,w3,w4,w5):
  dists=[]
  a=[w1,w2,w3,w4,w5]
  for i in a:
    dist=len(str(i))
    dists.append(dist)
  print(a,dists)
shet_letters("dgwd","111","wdwddwdw","12345","123456")
    
    #new   Вводится строка, включающая строчные и прописные буквы. Требуется вывести ту же строку в одном регистре, который зависит от того, каких букв больше. При равном количестве преобразовать в нижний регистр. Например, вводится строка "HeLLo World", она должна быть преобразована в "hello world", потому что в исходной строке малых букв больше. В коде используйте цикл for, строковые методы upper() (преобразование к верхнему регистру) и lower() (преобразование к нижнему регистру), а также методы isupper() и islower(), проверяющие регистр строки или символа.
def low_big_registr(stroka):
  low=0
  big=0
  for i in stroka:   
    if i.islower()==True:
      low+=1
    else:big+=1
  if low>big:
    print(stroka.lower())
  else:print(stroka.upper())
low_big_registr("ФАМИЛИЯ малеенькими буквами")
# new Строковый метод isdigit() проверяет, состоит ли строка только из цифр. Напишите программу, которая запрашивает с ввода два целых числа и выводит их сумму. В случае некорректного ввода программа не должна завершаться с ошибкой, а должна продолжать запрашивать числа. Обработчик исключений try-except использовать нельзя.

def summ_only_dig(a,b):
  if a.isdigit()==True and b.isdigit()==True:
    summa=a+b
  else:
    while a.isdigit()!=True and b.isdigit()!=True:
      b=input()
      a=input()
    summa=a+b
  print(summa)
summ_only_dig(4,"ededed")
# ысысс
def summ_only_dig():
  a=input("1 символ(строка или число)    ")
  b=input("2 символ(строка или число)    ")
  if a.isdigit()==True and b.isdigit()==True:
    summa=a+b
  else:
    while a.isdigit()!=True and b.isdigit()!=True:
      b=input()
      a=input()
    summa=a+b
  print(summa)
summ_only_dig()


# 1
# Дана строка, состоящая ровно из двух слов, разделенных пробелом. Переставьте эти слова местами. Результат запишите в строку и выведите получившуюся строку.

# При решении этой задачи нельзя пользоваться циклами и инструкцией if.

# Входные данные
# Вводится строка.

# Выходные данные
# Выведите ответ на задачу.

# Примеры
# Входные данные
# Hello, world!
# Выходные данные
# world! Hello,
stroka=str(input("Строку пожалуйста   "))
str_mass=stroka.split()
str_mass.reverse()
print(" ".join(str_mass))

# Дана строка. Найдите в этой строке второе вхождение буквы f, и выведите индекс этого вхождения. Если буква f в данной строке встречается только один раз, выведите число -1, а если не встречается ни разу, выведите число -2.
# При решении этой задачи нельзя использовать метод count.
stroka=str(input("Строку пожалуйста   "))
first_index=stroka.find("f")
result=stroka.find("f",first_index+1)
if "f" not in stroka:
  result=-2
print(result)

# Дана строка, в которой буква h встречается минимум два раза. Удалите из этой строки первое и последнее вхождение буквы h, а также все символы, находящиеся между ними.
stroka=str(input("Строку пожалуйста   "))
first_index=stroka.find("h")
last_index=stroka.rfind("h")
stroka=stroka[:first_index]+stroka[last_index+1:]
print(stroka)

# Дана строка, в которой буква h встречается как минимум два раза. Разверните последовательность символов, заключенную между первым и последнием появлением буквы h, в противоположном порядке.
stroka=str(input("Строку пожалуйста   "))
first_index=stroka.find("h")
last_index=stroka.rfind("h")
stroka=stroka[:first_index]+stroka[first_index+1:last_index].reverse()+stroka[last_index+1:]
print(stroka)
# Дана строка. Замените в этой строке все цифры 1 на слово one.
stroka=str(input("Строку пожалуйста   "))
print(stroka.replace("1","one"))
# Дана строка. Удалите из этой строки все символы @.
stroka=str(input("Строку пожалуйста   "))
print(stroka.remove("@"))






