n=int(input())
m=int(input())
bridges=[]
numset=set()
allset = set(range(1,n+1))
check_dict={}

for i in range(m):
  pair=input().split(' ')
  bridges.append(pair)

  if 0<i<=n:
    check_dict[i]=0

for el in range(len(bridges)):
  check_dict[int(bridges[el][0])]+=1
  check_dict[int(bridges[el][1])]+=1

  if  allset!= numset:
    numset.add(int(bridges[el][0]),int(bridges[el][1]))

  elif  allset== numset: 
    max_el= sorted()
     int((check_dict.values()+check_dict.keys()).sort( reverse=True)[0]) #максимальное значение 

    rec()


print(eval("пять"))


# def rec(n):




