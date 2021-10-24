# Напишите класс Snow по следующему описанию.

# В конструкторе класса инициируется поле, содержащее количество снежинок, выраженное целым числом.

# Класс включает методы перегрузки арифметических операторов: __add__() – сложение, __sub__() – вычитание, __mul__() – умножение, __truediv__() – деление. В классе код этих методов должен выполнять увеличение или уменьшение количества снежинок на число n или в n раз. Метод __truediv__() перегружает обычное (/), а не целочисленное (//) деление. Однако пусть в методе происходит округление значения до целого числа.

# Класс включает метод makeSnow(), который принимает сам объект и число снежинок в ряду, а возвращает строку вида "*****\n*****\n*****…", где количество снежинок между '\n' равно переданному аргументу, а количество рядов вычисляется, исходя из общего количества снежинок.

# Вызов объекта класса Snow в нотации функции с одним аргументом, должен приводить к перезаписи значения поля, в котором хранится количество снежинок, на переданное в качестве аргумента значение.
import random
class snow:
  def __init__(self,count):
    self.count=count
  def __add__(self,n):
    self.count+=n
  def __truediv__(self,n):
    self.count/=n
    self.count.round()
  def __mul__(self,n):
    self.count*=n
  def __sub__(self,n):
    self.count-=n
  def __call__(self,ch1,ch2):
    self.ch2=ch2
    self.list_count=ch1
    self.makeSnow(ch1)
    print(ch2)
  def makeSnow(self,list_count):
    self.list_count=list_count
    self.count_str=self.count//self.list_count
    self.string=str(("*"*self.list_count)+"\n")
    if self.count/self.list_count==0:
      print(self.count_str*self.string)
    else:
      print(self.count_str*self.string+("*"*(self.count%self.list_count)))
  def make_random_snow(self,min_list_count):
    self.min_list_count=min_list_count
    self.count_str=self.count//self.min_list_count
    for strs in range(0,self.count_str):
      self.list_count=random.randint(self.min_list_count,50)
      self.string = "*" * self.list_count
      if 40<=self.list_count<70:self.random_space=random.randint(0, 2)
      elif 30<=self.list_count<40:self.random_space=random.randint(1, 3)
      elif 20<=self.list_count<30:self.random_space=random.randint(1, 5)
      elif 10<=self.list_count<20:self.random_space=random.randint(2, 7)
      elif 0<self.list_count<10:self.random_space=random.randint(4, 15)
      for elem in self.string:
        elem +=(" "*self.random_space)
        print(elem, end="")
      print("\n")
  def __call__(self,change):
    self.count=change
snow1=snow(100)
snow1.makeSnow(10)
# snow1.make_random_snow(20)
snow1(25)
print(snow1.count+5)
print(snow1.count/5)
print(snow1.count*5)
print(snow1.count-5)

# snow1(25,25)
# snow1.makeSnow(9)
# snow1.make_random_snow(12)
# print(snow1.count+5)
# print(snow1.count/5)
# print(snow1.count*5)
# print(snow1.count-5)