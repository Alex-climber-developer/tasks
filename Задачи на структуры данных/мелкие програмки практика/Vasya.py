v=int(input("введите скорость Васи  "))
t=int(input("введите время Васи в пути    "))
s=109

if v<0:
  s=v*t
  s=109+s
else:  
  s=v*t
if s>109:
  s=s-109
if s<-109:
  s=109-(-s-109)

print(s)

# Вариант без условий,не работает верно
v=int(input("введите скорость Васи  "))
t=int(input("введите время Васи в пути    "))
s=109

try:
  v<0
  s=v*t
  s<-109
  s=109-(-s-109)
except:
  try:
    s>-109
    s=109+s
  except:
      None
    
try:
    v>0
    s=v*t
    s<109
except:
    try:
      s>109
      s=s-109
    except:
      None
    
  
print(s)
