a = str(input("введите число от 1 до 100-  "))
ch = [0, 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'L', 'C'] # создаем массив верных римских,с удобными,,считабельными,,индексами(поэтому 1эл левый)
alert = 0 # переменная вывода
N = len(str(a))-1 # ищем длину числа минус один дабы сделаать поиск по индексам(j)
for j in range(0,N): #поиск по индексам для разных проверок с "j"
     for i in range(1, 10): #поиск ЦИФРЫ
          if str(i) == a[j]: # проверка равенства цифры с цифрой в нашем числе(1ой или 2ой)
                if 10 > int(a) >= 1: #а вдруг это однозначное число???!!
                    alert = ch[i]
                elif 40 >int(a) >= 10: #проверка до 40ка
                    if j == 0:
                        alert = i * ch[10]
                    if j == 1:
                        if i == 0:
                            None #не нужно нам ничего писать в эт случае
                        else:
                            alert = alert + ch[i]
                elif 90 >int(a)>= 40:   #проверка нашего числа в этом диапазоне
                    if j == 0 and i == 4:        # если это 1ая ЦИФРА =4
                        alert = ch[10]+ch[11]         # запоминаем число десятков=4
                    elif j == 1:     # Для 2ой цифры от 1 до 9
                        if i == 0:
                            None
                        else:
                            alert = alert+ch[i] # прибавить 2ую цифру у числа
                    if j == 0 and 4<i<9:  # проверка числа на десятки в этом диапазоне
                      alert =ch[11] + (i-5) * ch[10]  # формула для десятков
                    elif j == 0 and i==9:  # проверка числа на десятки в этом диапазоне
                      alert =ch[10] +ch[12]  # формула для десятков
                    elif j == 1:
                        if i == 0:
                            None
                        else:
                            alert = alert + ch[i]  #ф-ла для едениц
                    if a=="100":
                      alert=ch[12]
print(alert)