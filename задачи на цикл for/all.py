# Входные данные
# Вводятся 4 числа: a, b, c и d. 

# Выходные данные
# Выведите все числа на отрезке от a до b, дающие остаток c при делении на d. Если таких чисел не существует, то ничего выводить не нужно.

answ=[]
a=int(input("Введите число начала отрезка_  "))
b=int(input("Введите число начала отрезка_  "))
c=int(input("Введите число просто так_  "))
d=int(input("Введите число для деления_  "))
for i in range(a,b+1):
  if i%d!=0:
    answ.append(i)
for j in answ:print(j,sep=", ") 

# Входные данные
# Вводятся целые числа a и b. Гарантируется, что a не превосходит b.

# Выходные данные
# Выведите все числа на отрезке от a до b, являющиеся полными квадратами. Если таких чисел нет, то ничего выводить не нужно.

# Примеры
# Входные данные
# 2
# 8
# Выходные данные
# 4 

def square_dist(a,b):
  for i in range(a,b+1):
    for x in range(0,b+1):
      if i==x**2:
        print(i)
square_dist(1,1000)

# Найдите самый маленький натуральный делитель числа x, отличный от 1 (2 <= x <= 30000).

def NOD(x):
  for i in range(2,x):
    if x%i==0:
      print(i)
      break
NOD(121)
# Выведите все натуральные делители числа x в порядке возрастания (включая 1 и само число).

def all_OD(x):
  for i in range(1,x+1):
    if x%i==0:
      print(i)
all_OD(100)

# Входные данные
# Вводятся 4 числа: a, b, c и d.

# Выходные данные
# Найдите все целые решения уравнения ax3 + bx2 + cx + d = 0 на отрезке [0,1000] и выведите их в порядке возрастания.  Если на данном отрезке нет ни одного решения, то ничего выводить не нужно.

def prav_lin_yr_3stepiny(a,b,c,d):
  answ=[]
  #ax^3 + bx^2 + cx + d = 0
  for x in range(0,1001):
    if a*x**3 + b*x**2 + c*x + d ==0:
      answ.append(x)
  if len(answ)==0:print("")
  else:print(sorted(answ))
prav_lin_yr_3stepiny(4,-0,1,0)


# # Вычислите N! – произведение всех натуральных чисел от 1 до N ( N!=1∙2∙3∙…∙ N ).

# Входные данные
# Вводится единственное число N – натуральное, не превосходит 12.

# Выходные данные
# Выведите полученное значение N!

# (рекомендуется решить двумя способами - с циклами и с помощью рекурсивной функции)
def factorial(N):
  for i in range(N-1,0,-1):
    N=N*i
  print(N)
factorial(3)
# рекурсивн метод
def factorial(N):
  while N>=2:
    N=N*factorial(N-1)
    N-=1
  return N
factorial(5)
# Напишите программу, вычисляющую 2^N.

# Входные данные
# Вводится целое неотрицательное число N, которое не превосходит 30.

# Выходные данные
# Выведите число 2^N.

# (рекомендуется решить двумя способами - с циклами и с помощью рекурсивной функции)
def stepen2N(N):
  print(2**N) 
stepen2N(10)


# 2rote
def stepen2N(N):
  answ=1
  for i in range(0,N):
    answ=answ*2
  print(answ)
stepen2N(10)

#Полиндромы от 1 до n вкл в 2ном виде самого числа n
N=int(input("Введите верхнюю границу поиска полиндромов(натур-е число) "))
for i in range(1,N+1,2):
  if int(bin(i)[2:])== int(format(i,'b')[::-1]):
    if not [False for j in range(2,i) if i%j==0]:
        print(i," (%d)" %int(format(i,'b')))


#https://sun1-84.userapi.com/RQhlxhjK0KeSYMRXpgyBrdaiN..
def next_digit(n):
  next_digit=''
  count=1
  for i in str(n):
    if str(n).index(i)==len(str(n))-1:
      next_digit+=str(count)+i
      break
    if n[str(n).index(i)+1]==i: count+=1
    else: next_digit+=str(count)+i
    return next_digit
def easy_digits_num(k,start):
  if k==1:
    return start
    easy_digits_num(k-1, next_digit(start))
easy_digits_num(5, 1)