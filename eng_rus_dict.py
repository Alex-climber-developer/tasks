# x={'y': ["a","b"],"":["b","c"],"w ":["a","c","d"]}
y={}
strg=''
n=int(input())
x={}
for i in range(n):
  strg+=input()
  eng=strg.split('-')[0]
  eng_ost=strg.split('-')[1]
  rus=[]
  for j in eng_ost.split(','):
    if j[0]==' ' and j[-1]==' ' : rus.append(j[1:-1])
    elif j[0]!=' ' and j[-1]==' ' : rus.append(j[:-1])
    elif j[0]==' ' and j[-1]!=' ' : rus.append(j[1:])
    else:rus.append(j)
  x[a]=rus
  
print(x)
