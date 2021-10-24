# a=[]
# b=[ 0 if x==1 else x for x in a if x>0]

A=[89,5,7,3,5,1,4,8,4,3,5,98,42,24,55,78,97,3]
def ins_s(a):
  b=[a[0]]
  for ia in range(1,len(a)):
    for ib in range(-1,-len(a),-1):
      if a[ia] > b[ib]: b.append(a[ia])
      elif ib==-1 or ib==0: b[ib], a[ia] = a[ia], b[ib]
      else: b.insert(ib, a[ia])
  print(b)
ins_s(A)