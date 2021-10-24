y={}
x={}

n=int(input("введите колво строк "))
for i in range(n):
  strg=input('введите строку ')
  eng=strg.split('-')[0]
  eng_ost=list(strg.split('-'))[1]
  rus=[]

  for j in eng_ost.split(','):

    if j[0]==' ' and j[-1]==' ' : rus.append(j[1:-1])
    elif j[0]!=' ' and j[-1]==' ' : rus.append(j[:-1])
    elif j[0]==' ' and j[-1]!=' ' : rus.append(j[1:])
    else:rus.append(j)

  x[eng]=rus

# y={}
# x={'x': ["a","b"],"y":["b","d"],"z ":["a","c","d"]}
for k,v in x.items():
  for i in v:
    if y.get(i)==None:
      y[i]=[k]
    else:
      y[i].append(k)
# (y.get(v[i]))


for key,val in y.items():
  print(key,"-",','.join(val))