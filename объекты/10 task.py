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


