def test():
    N=int (input("Введите число  "))
    if N>0:
        return
        def positive():
            print("Положительное")
    elif N<0:

        def negative():
            print("Отрицательное")
            return
    elif N==0:
        def null():
            print("Ноль")
test()

# новый
S = 0
r = 0
import math


def cylinder():
    def circle():
        global r
        r = int(input("Введите радиус  "))
        global S
        S = math.pi * r * r

    answ = str(input("Вам нужна площадь боковой поверхности цилиндра или полная площадь цилиндра :  ДА/НЕТ    "))
    h = int(input("Введите высоту  "))
    if answ == "НЕТ":
        S = math.pi * r * h + 2 * S

    else:
        S = 2 * math.pi * r * h
    return S


square=cylinder()
print(square)
def returner():
  res=1
  while True:
    i= int(input())
    if i!=0:
      res=res*i
    if i==0:
      break
  return res
returner()

# new2

def testInput(inp):
  inp=input()
  if type(inp)==int or type(inp)==float:
    return inp
  else:print("It is not a int input")
res= testInput("dsfwefwas")
print(res)
# new3

def printInt(inp):
  return inp
res= printInt("test str")
print(res)
round(33234579.378987654,9)
# new юникод возвратить символ по номеру,пока не "0"

def unic():
  while True:
    i= chr(input())
    if i!=0:
      return i
    if i==0:
      break
unic()

# new num 10
A = int(input("введите число 1:   "))
B = int(input("введите число 2:   "))
while A != B:
    if A % 2 == 0 and A >= B*2:
        A = A/2
        print(':2')
    else:
        A = A-1
        print("-1")

# newwwwwww
count = 0
maxel = 0
ch = []

while i != 0:
    i = int(input("введите число   "))
    ch.append(i)
N = len(ch)
for w in range(0, N):
    if ch[w+1] == ch[w]:
        count += 1
        j += 1
    elif ch[w-1] != ch[w]:
        count += 1
        if maxel < count:
            maxel = count
print(maxel)

#new
def test():
    N=int (input("Введите число  "))
    if N>0:
        def positive():
            print("Положительное")
    elif N<0:
        def negative():
            print("Отрицательное")
    elif N==0:
        def null():
            print("Ноль")
test(N)


#########
S=0
r=0
import math
def cylinder():

    def circle():
        global r
        r=int (input("Введите радиус  "))
        global S
        S= math.pi*r*r
    answ=str(input("Вам нужна площадь боковой поверхности цилиндра или полная площадь цилиндра :  ДА/НЕТ    "))
    h=int (input("Введите высоту  "))
    if answ== "НЕТ":
        S=math.pi*r*h+2*S
        
    else:
        S=2* math.pi*r*h
    return S
cylinder()