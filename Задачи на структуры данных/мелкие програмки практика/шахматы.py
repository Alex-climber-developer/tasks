our_x=int(input("введите координату вашего 'Х'"))
our_y=int(input("введите координату вашего 'Y'"))
their_x=int(input("введите координату противника 'Х'"))
their_y=int(input("введите координату противника 'Y'"))
count=0
for i in range(1,8):
  if their_x==our_x + i and their_y==our_y + i:
    print("Yes")
  else:
    count+=1
for i in range(-7,0):
  if their_x==our_x + i and their_y==our_y + i:
    print("Yes")
  else:
    count += 1
if count==14:
  print("No")