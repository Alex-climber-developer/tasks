# Создайте файл nums.txt, содержащий несколько чисел, записанных через пробел. Напишите программу, которая подсчитывает и выводит на экран общую сумму чисел, хранящихся в этом файле.
mas=[]
summa=0
for stroka in open("nums.txt"):
  mas.append(stroka.split())
for i in mas:
  summa+=int(i)
print(summa)
    