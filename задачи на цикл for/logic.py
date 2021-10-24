count=int(input("Введите колличество переменных "))
table=[]
sum_1=0
flag=0
no="¬"
result=''
for i in range(0,count+1):
  output=''
  if i==count:output="вывода "
  name=input("Введите название переменной %s "%output).upper()
  table.append({name:input("Введите без пробелов и запятых нули и единицы для %s %s "%(output,name))})
for res in table[-1].values()[0]:
  sum_1+=int(res)
if len(table[-1].values()[0])//2<=sum_1: flag=1
if not(flag):result+='¬( '
string=''

for j in range(0,len(table[-1].values()[0])):
  if table[-1].values()[0][j]==flag:
    for x in range(0,len(table)):
      
      simvol= no * int(not(table[x].values()[0][j])) + table[x].keys()[0]
      string+=simvol+' * '
  result+=string+' + '
  if j==len(table[-1].values()[0])-1: result+=' ).'
print(result)
