# Практическое задание: композиция
# Приведенная в теоретическом блоке программа имеет ряд недочетов и недоработок. Требуется исправить и доработать, согласно следующему плану.

# При вычислении оклеиваемой поверхности мы не "портим" поле self.square. В нем так и остается полная площадь стен. Ведь она может понадобиться, если состав списка wd изменится, и придется заново вычислять оклеиваемую площадь.

# Однако в классе не предусмотрено сохранение длин сторон, хотя они тоже могут понадобиться. Например, если потребуется изменить одну из величин у уже существующего объекта. Площадь же помещения всегда можно вычислить, если хранить исходные параметры. Поэтому сохранять саму площадь в поле не обязательно.

# Исправьте код так, чтобы у объектов Room были только четыре поля – width, lenght, height и wd. Площади (полная и оклеиваемая) должны вычислять лишь при необходимости путем вызова методов.

# Программа вычисляет площадь под оклейку, но ничего не говорит о том, сколько потребуется рулонов обоев. Добавьте метод, который принимает в качестве аргументов длину и ширину одного рулона, а возвращает количество необходимых, исходя из оклеиваемой площади.

# Разработайте интерфейс программы. Пусть она запрашивает у пользователя данные и выдает ему площадь оклеиваемой поверхности и количество необходимых рулонов.

class Win_door:
  def __init__(self,h,w):
    self.w=w
    self.h=h
  def square_wd(self):
    self.square_wd=self.w * self.h
    return self.square_wd

class Room:
  def __init__(self,h,w,l):
    self.width=w
    self.height=h
    self.lenght=l
    self.wd=[]
  def change(self, h, w, l):
    if h==0:None
    else:self.height=h
    if w==0:None
    else:self.width=w
    if l==0:None
    else:self.lenght=l
  def square_start_room(self):
    self.square_start_room=2 * self.height * (self.width + self.lenght)
    return self.square_start_room
  def add_wd(self,h,w):
    self.wd.append(Win_door(h, w))
  def square_finish_room(self):
    st_room=self.square_start_room()
    self.square_finish_room =st_room
    for win_door in self.wd:
      self.square_finish_room-=win_door.square_wd
    return self.square_finish_room

class feetback:
  def offer(self):
    print(
      "Я бы мог тебе предложить более выгодные габариты обоев ,но пока такой функции нет,номер карты на donat будет выдан автоматически")
    return self.donat()
  def donat (self):
    print("Если ты это читаешь то тебе не повезо с обоями,вот номер карты для дальнейшего улучшения сервиса-000000000000")
    input()

class rylon:
  def __init__(self, w, h):
    self.w_ryl=w
    self.h_ryl=h
    self.count_ryl=Room.square_finish_room()/int(self.w_ryl*self.h_ryl)
    if self.count_ryl % 1>0.5:
      feetback.offer()
    if self.count_ryl % 1>0.8:
      print("ну не повезло,нафига тебе столько лишних обоев теперь...")
    if int( self.count_ryl ) == False: self.count_ryl = self.count_ryl+1-self.count_ryl%1
    print("Если длина рулона-%d , а ширина- %d , то вам нужно %d рулонов" % (self.h_ryl, self.w_ryl, self.count_ryl))
r1 = Room(20,30,10)
r1.add_wd(2,3)
r1.add_wd(3,2)
r1.add_wd(2,2)
r1.add_wd(1,1)
print(r1.square_finish_room())
r1.change(10,15,17)
print(r1.square_finish_room())

