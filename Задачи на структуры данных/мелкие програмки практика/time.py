chas1=int(input("введите колличество часов в 1 момент "))
min1=int(input("введите колличество минут в 1 момент "))
sec1=int(input("введите колличество секунд в 1 момент "))
chas2=int(input("введите колличество часов в 2 момент "))
min2=int(input("введите колличество минут в 2 момент "))
sec2=int(input("введите колличество секунд в 2 момент "))
beetwen=(sec2+min2*60+chas2*3600)-(sec1+min1*60+chas1*3600)
print(beetwen,"sec")

# new prog
n=int(input("введите колличество школьников  "))
k=int(input("введите колличество яблок  "))
poor= n-(k%n)
print(poor, "несчастных")

# new

h=int(input("введите длину шеста "))
a=int(input("введите колличество метров подъема "))
b=int(input("введите колличество метров спуска  "))
dist_day=a-b
day=0
while dist_day<h:
  day+=1
  dist_day += a
  if dist_day>=h:
    break
  else:
    dist_day -= b

print("шел", day+1 ," день")



# new
ch=str(input("введите число "))


