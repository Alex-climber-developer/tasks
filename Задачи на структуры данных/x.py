n=int(input())
k=int(input())
k_buz=1
peoples= {}

def cut_time(string):
  if string[0]==0:
    minuts=int(string[1])
  else: minuts=int(string[0:2])
  
  if string[3]==0:
    ours=int(string[4])
  else: ours=int(string[3:5])

  return [minuts,ours]


for i in range(n):
  info=input().split(' ')
  info[1]=cut_time(info[1])
  info[2]=cut_time(info[2])

  peoples[info[0]]=[info[1],info[2]]
  
times=peoples.values()


for ind in range(0,len(times)):
  # if k==0:
  #   k_buz=0
  #   break
  if times[ind][1] > times[ind+1][0] and k_buz<k:
    k_buz+=1




