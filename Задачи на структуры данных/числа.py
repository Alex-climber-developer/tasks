A= int(input("введите число 1:   "))
B = int(input("введите число 2:   "))
while A!=B:
    if A%2==0 and A>=B*2:
        A=A/2
        print(':2')
    else:
        A=A-1
        print("-1")


# нов
count = 0
maxel = 0
ch = []
i=''
while i != 0:
    i = int(input("введите число   "))
    ch.append(i)
N = len(ch)
for w in range(0, N-1):
    if ch[w+1] == ch[w]:
        count += 1
        w += 1
    elif ch[w-1] != ch[w]:
        count += 1
        if maxel < count:
            maxel = count

# новый
print(maxel)

# добавление "*" до 10ти
My_str=input()
if len(My_str)<10:
  new_str=My_str+"*"*(10-len(My_str))
  print(new_str)
elif len(My_str)>10:
  print("Try again,its so mush")

  # new мин макс округленные до 2 знакаа

  def min_max_2():
    max=-100000
    min=1000000
    mass=[]
    for i in range(0,6):
      a=float(input("число  "))
      mass.append=round(a,2)
      if mass[i]>max:
        max=mass[i]
      elif mass[i]<min:
        min=mass[i]
    return min ,max
a=min_max_2()
print(a)
# new мин макс сумм
a=[]
i=0
while i<8:
  ch=int(input("число  "))
  a.append(ch)
  i+=1

summa=sum(a)
minimum=min(a)
maximum=max(a)
print("minimum: %d , maximum: %d , summa: %d ." %(minimum, maximum, summa))


# new вывести по 10 зн рандом флота ,отсортировать и вывести снова
import random
b=[]
i=0
stroka=""
while i<100:
  ch=round(random.random()*(100-5)+5, 2)
  if i%9==0:
    ch=str(ch)+"\n"
  b.append(ch)
  i+=1
print(b)
input("нажмите enter ")
b=b.sort()
for i in b:
  if i%9==0:
    i=str(i)+"\n"

# new Заполните список случайными числами. Используйте в коде цикл for, функции range() и randint().
from random import randint
s=[]
for i in range(10):
  n=randint(0,100)
  s.append(n)
print(s)
#new В заданном списке, состоящем из положительных и отрицательных чисел, посчитайте количество отрицательных элементов. Выведите результат на экран.

def shet_minus(a,s,d,f,g,h,j,k,l,q):
  minus=0
  plus=0
  a=[a,s,d,f,g,h,j,k,l,q]
  for i in a:
    if i<0:
      minus+=1
    else:plus+=1
  print(minus, plus)
shet_minus(1,-23,455,-34546,132,-5,-7,543,-22,-2)
    
    #new Напишите программу, которая заполняет список пятью словами, введенными с клавиатуры, измеряет длину каждого слова и добавляет полученное значение в другой список. Например, список слов – ['yes', 'no', 'maybe', 'ok', 'what'], список длин – [3, 2, 5, 2, 4]. Оба списка должны выводиться на экран.

