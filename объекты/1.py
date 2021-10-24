# Есть класс "Боец". От него создаются два экземпляра-юнита. Каждому устанавливается определенный показатель здоровья (на выбор). В случайном порядке они бьют друг друга. Тот, кто бьет, здоровья не теряет. У того, кого бьют, оно уменьшается на определенное количество пунктов. После каждого удара надо выводить сообщение, какой юнит атаковал, и сколько у противника осталось здоровья. Как только у кого-то заканчивается ресурс здоровья, программа завершается сообщением о том, кто одержал победу.
import random
class warer:
  def setName(self,n):
    self.name=n
  healf=100
  healf_minus=0
  def healf_down(self):
    self.healf_minus=random.randint(1,5)
    self.healf-=self.healf_minus
    print("У противника осталось %d здоровья" %self.healf)
  def war(self):
    print("\nАтаковал ", self.name)

joun1=warer()
joun1.setName("Воин 1")
joun2=warer()
joun2.setName("Воин 2")
step_j1=0
step_j2=0
while joun1.healf>0 and joun2.healf>0:
  step=random.randint(2,100)
  if step%2==0:
    joun2.war()
    joun1.healf_down()
    step_j2+=1
  else:
    joun1.war()
    joun2.healf_down()
    step_j1+=1
print("1 воин атаковал %d раз, 2ой- %d раз"%(step_j1,step_j2))
if joun1.healf<=0:print("Победил Воин 2")
elif joun2.healf<=0:print("Победил Воин 1")






# Есть класс Person, конструктор которого принимает три параметра (не учитывая self) – имя, фамилию и квалификацию специалиста. Квалификация имеет значение заданное по умолчанию, равное единице.

# У класса Person есть метод, который возвращает строку, включающую в себя всю информацию о сотруднике.

# Класс Person содержит деструктор, который выводит на экран фразу "До свидания, мистер …" (вместо троеточия должны выводиться имя и фамилия объекта).

# В основной ветке программы создайте три объекта класса Person. Посмотрите информацию о сотрудниках и увольте самое слабое звено.

# В конце программы добавьте функцию input(), чтобы скрипт не завершился сам, пока не будет нажат Enter. Иначе вы сразу увидите как удаляются все объекты при завершении работы программы.
class Person:
  def __init__(self,name,last_name,category=1):
    self.name=name
    self.last_name=last_name
    self.category=category
  def my_info(self):
    print("Добрый день ,меня зовут %s %s , я профессиональный мастер %d категории" %(self.name,self.last_name,self.category))
  def __del__(self):
    print("До свидания, мистер %s %s" %(self.name, self.last_name))
p1=Person("Саша","Брюфилов",2)
p2=Person("Дима","Кузин",4)
p3=Person("Петя","Лейбун",3)
list_p=[p1,p2,p3]
cat=[]
for people in list_p:
  cat.append (people.category)
cat=sorted(cat)
for i in list_p:
  i.my_info()
  if i.category==cat[0] or i.category==cat[1]:
    i.__del__()
  else:print ("а вот вас то %s мы и примем" %i.name)
input()


# Практическое задание: Наследование
# Разработайте программу по следующему описанию.

# В некой игре-стратегии есть солдаты и герои. У всех есть свойство, содержащее уникальный номер объекта, и свойство, в котором хранится принадлежность команде. У солдат есть метод "иду за героем", который в качестве аргумента принимает объект типа "герой". У героев есть метод увеличения собственного уровня.

# В основной ветке программы создается по одному герою для каждой команды. В цикле генерируются объекты-солдаты. Их принадлежность команде определяется случайно. Солдаты разных команд добавляются в разные списки.

# Измеряется длина списков солдат противоборствующих команд и выводится на экран. У героя, принадлежащего команде с более длинным списком, поднимается уровень.

# Отправьте одного из солдат первого героя следовать за ним. Выведите на экран идентификационные номера этих двух юнитов.
import random
class man:
  def __init__(self,num,comand):
    self.num=num
    self.comand=comand
class hero(man):
  skill=0
  def up_skill(self,n):
    self.skill+=n
class soldat(man):
  def go_to(self,hero):
    print("Иду за героем")
hero1=hero(1,"first")
hero2=hero(2,"second")
count_soldat=int(input("введите число солдат в игре   "))
first_comand=[]
second_comand=[]
for i in range(1,count_soldat+1):
  name=str("soldat "+str(i))
  j=random.randint(3,4)
  if j%2==0:com="first"
  else:com="second"
  name=soldat(i,com)
  if name.comand.lower()=="first":first_comand.append(name)
  else:second_comand.append(name)


print("Длина 1 команды= %d , 2ой= %d" %(len(first_comand),len(second_comand)))
if len(first_comand)>len(second_comand):
  hero1.up_skill(len(first_comand)-len(second_comand))
  print("У 1ого героя %d очков"%hero1.skill)
else:
  hero2.up_skill(len(second_comand)-len(first_comand))
  print("У 2ого героя %d очков"%hero2.skill)
s=random.randint(1,len(first_comand))
for x in first_comand:
  if first_comand[s]==x:
    print("солдат сказал: ")
    x.go_to(1)
    print("Номер верного солдата-%d ,номер доблестного героя- %d"%(x.num,hero1.num))
    break


# Практическое задание: метод перезагрузки оператора сложения
# Попробуйте самостоятельно перегрузить оператор сложения. Для его перегрузки используется метод __add__(). Он вызывается, когда объекты класса, имеющего данный метод, фигурируют в операции сложения, причем с левой стороны. Это значит, что в выражении a + b у объекта a должен быть метод __add__(). Объект b может быть чем угодно, но чаще всего он бывает объектом того же класса. Объект b будет автоматически передаваться в метод __add__() в качестве второго аргумента (первый – self).
# Отметим, в Python также есть правосторонний метод перегрузки сложения - __radd__().
# Согласно полиморфизму ООП, возвращать метод __add__() может что угодно. Может вообще ничего не возвращать, а "молча" вносить изменения в какие-то уже существующие объекты. Допустим, в вашей программе метод перегрузки сложения будет возвращать новый объект того же класса.
# import types
class persons:
  def __init__(self,count1,count2,count3):
    self.count_arm=count1
    self.count_knoledge=count2
    self.count_teef=count3
  def __add__(self,value):
    self.a+=value.a
    self.b+=value.b
    self.c+=value.c
  a="руки"
  b="мыслей"
  c="зубов"
  def my_info(self):
    print(F"Это мои-{self.count_arm} {self.a},{self.count_knoledge} {self.b},{self.count_teef} {self.c}.")
first_pers=persons(2,38,29)
second_pers=persons(3,12,150)
first_pers.my_info()
second_pers.my_info()
# Это мои-2 руки,38 мыслей,29 зубов.
# Это мои-3 руки,12 мыслей,150 зубов.
print(first_pers.a+" "+second_pers.a) # руки руки
print(first_pers.b+" "+second_pers.b)# мыслей мыслей
print(first_pers.c+" "+second_pers.c) # зубов зубов
print(first_pers+second_pers) # None


