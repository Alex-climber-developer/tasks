def div(n,m):
  make_minus = False
  if (n < 0 and m > 0) or (n > 0 and m < 0):
    make_minus = True

  n,m = abs(n), abs(m)
  count_approx= int(input(' enter a count digit after point:  '))
  result=''
  count_approx_now= 0
  COUNT_POS = 0
  if int(str(n)[:len(m):]) >= m :
    ost = int(str(n)[:len(m):])
  else: ost = int(str(n)[:len(m)+1:])

  while n > 0:

    result+= str(ost//m)
    ost%= m
    if ost==0:
      result+='0'
      ost=''
    if int(str(ost) + str(n)[len(m)+COUNT_POS : len(m)+COUNT_POS+1]) >= m:
      ost= int(str(ost) + str(n)[len(m)+COUNT_POS : len(m)+COUNT_POS+1 ])
      COUNT_POS+=1
    else:
      
      ost= int(str(ost) + str(n)[len(m)+COUNT_POS : len(m)+COUNT_POS+2 ])
      COUNT_POS+=2

    if count_approx == count_approx_now : break
    if ost < m and count_approx_now < count_approx:
      if count_approx_now == 0 : result+='.'
      count_approx_now+=1
      ost*= 10

    

  if make_minus: return '-' + result
  else: return result



def multi(n,m):
  make_minus = False
  result=0

  if (n < 0 and m > 0) or (n > 0 and m < 0):
    make_minus = True
  n,m = abs(n), abs(m)


  n=str(n);m=str(m)
  if len(n) < len(m):
    n,m = m,n
  n_mas,m_mas = [i for i in n[::-1]], [j for j in m[::-1]]
  lines=[ '' ] * len(m)

  for ind_m in range(0,len(m_mas)):
    rem= 0
    for ind_n in range(0,len(n_mas)):
      step = str(int(m_mas[ind_m]) * int(n_mas[ind_n]) + rem)
      if len(n_mas)> ind_n+1:

        if len(step) > 1:
          rem, step = int(step[0]), step[1]
        else: rem = 0
        lines[ind_m]+= (step)

      else:
        lines[ind_m]+= step[::-1]
        lines[ind_m] = lines[ind_m][::-1]

  for el_mas in range(1,len(lines)):
    lines[el_mas] = int(lines[el_mas]) * (10**el_mas)

  for el in lines: result+= int(el)
  if make_minus: return result* -1
  else: return result



def summ(n,m):
  make_minus = False

  if n < 0 and m > 0:
    return diff(m,-n)
  elif n < 0 and m < 0:
    make_minus = True
    n,m = -n, -m
  elif n > 0 and m < 0:
    return diff(n,-m)

  result = ''
  rem = 0
  n=str(n)[::-1];m=str(m)[::-1]

  if len(n)!= len(m):
    if len(n)> len(m): m+='0' * (len(n) - len(m))
    else: n+='0' * (len(m) - len(n))

  for i in range(0,len(n)):
    step = str(int(n[i])+int(m[i])+rem) 
    if len(step) > 1:
      if i == len(n)-1:
        step= step[::-1]
      else: rem, step = int(step[0]), step[1]
    else:rem = 0
    result+= step
    
  if make_minus: return int(result[::-1]) * -1
  else: return int(result[::-1]) 
  

 
def diff(n,m):
  result = ''
  loan = 0
  make_minus = False

  if n < 0 and m > 0:
    return summ(n,-m)
  elif n < 0 and m < 0:
    n,m = -m,-n
  elif n > 0 and m < 0:
    return summ(n,-m)

  if n < m:
    n,m = m,n
    make_minus = True
  elif n == m: return 0
  n=str(n)[::-1];m=str(m)[::-1]

  if len(n)!= len(m):
    if len(n)> len(m): m+='0' * (len(n) - len(m))
    else: n+='0' * (len(m) - len(n))

  for i in range(0,len(n)):
    if i == len(n)-1:
      if int(n[i])-loan != 0:
        result+= str(int(n[i]) - loan - int(m[i]))
        break
      else:break
    elif int(n[i]) - loan >= int(m[i]):
      step = str(int(n[i]) - loan - int(m[i]))
      loan = 0
    else:
      step = str(int(n[i])+10- loan - int(m[i]))
      loan = 1
    result+= step
  if make_minus: return int(result[::-1]) * -1
  else: return int(result[::-1]) 


while 1:
  inp_mas= str(input('2 digits and beetwen a sign (+-*/) with tabs or 0 if quit: ')).split(" ")
  if inp_mas == ['0']:
    print('thanks for using;  By')
    break
  else:
    try:
      n= int(inp_mas[0]); m= int(inp_mas[2])
    except:
      print('try again like i sad')
      continue

    if inp_mas[1] == '+':
      print('The answer is ' , summ(n,m), '\n')
    elif inp_mas[1] == '-' :
      print('The answer is ' ,diff(n,m), '\n')
    elif inp_mas[1] == '*':
      print('The answer is ' ,multi(n,m), '\n')
    elif inp_mas[1] == '/' :
      print('The answer is ' ,div(n,m), '\n')
    else: print('try again like i sad')