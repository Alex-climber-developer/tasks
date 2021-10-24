correct=False
while correct==False:
  name_connect=[bin(x)[2:]  if 0<=int(x)<=255 else -1 for x in  input("Введите имя узла компьютера через точку (в 10-ой СС)  ").split('.')]
  mask=[bin(x)[2:] if 0<=int(x)<=255 else -1 for x in input("Введите маску сети (в 10-ой СС)  ").split('.') ] 
  for i,j in zip(name_connect,mask):
    if i<0 or j<0: correct==False
    else:correct==True
print("".join([n*m for n,m in zip(name_connect ,mask) ]))




correct=0
result=''
while correct==0:
  correct=1
  name_connect= input("Введите имя узла компьютера через точку (в 10-ой СС)  ").split('.')
  mask=input("Введите маску сети (в 10-ой СС)  ").split('.')
  for x,y in zip(name_connect,mask):
    if 0<=int(x)<=255 and 0<=int(y)<=255 :
      mask[mask.index(y)]=bin(int(y))[2:] 
      name_connect[name_connect.index(x)]=bin(int(x))[2:] 
    else:
      print("Ошибка вода ,попробуйте все снова ")
      correct*=0
for n,m in zip(name_connect ,mask): result+=str(int(n)&int(m))
print(result)