def f(n):
  if n==21:
    return 1
  if n<21:
    return 0
  else:
    return f(n-1)+f(n-2)+f(n-5)
print(f(30))

#===============================

def g(n):
  if n==31:
    return 1
  if n<31:
    return 0
  else:
    return g(n-5)+g(n-4)+g(n-2)

for i in range(32, 100):
  if g(i)==1001:
    print(i)
    break
#===============================

def k(n):
  if n==2:
    return 1
  if n<2:
    return 0
  elif n%2==0 and n%1.5==0:
    return k(n-1)+k(n/1.5)
  else:
    return k(n-1)
print(k(22))

#===============================

def q(n,st):
  if n == st:
    return 1
  if n < st:
    return 0
  elif n%2==0:
    return q(n-1,st)+q(n-2,st)+q(n/2,st)
  else:
    return q(n-1,st)+q(n-2,st)
print(q(12, 10)+q(10, 7)+q(7, 1))

#===============================
#не до делано

count1=0
deeps=[]
def m(n,d):
  global deeps
  if n == 1:
    return 1
    deeps.append(d)
    # return count1
  if n < 1:
    return 0
    
  elif n%3==0:
    return m(n-1,d+1)+m(n-5,d+1)+m(n/3,d+1)

    # count1+=1
  else:
    return m(n-1,d+1)+m(n-5,d+1)
    # count1+=1

m(237,0)

print(min(deeps))