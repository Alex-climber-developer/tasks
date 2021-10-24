DICT={
  'один':1,
  'одна':1,
  'две':2,
  'два':2,
  'три':3,
  'четыре':4,
  'пять':5,
  'шесть':6,
  'семь':7,
  'восемь':8,
  'девять':9,
  'десять':10,
  'одинадцать':11,
  'двенадцать':12,
  'тринадцать':13,
  'четырнадцать':14,
  'пятнадцать':15,
  'шестнадцать':16,
  'семнадцать':17,
  'Восемнадцать':18,
  'Девятнадцать':19,
  'двадцать':20,
  'тридцать':30,
  'сорок':40,
  'пятьдесят':50,
  'шестьдесят':60,
  'семьдесят':70,
  'восемьдесят':80,
  'девяносто':90
}
KEY_WORD={
  'сто':100,
  'сти':100,
  'сот':100,
  'тысяч':1000,
  'миллион':10**6,
  'лям':10**6,
  'миллиард':10**9,
  'лярд':10**9,
  'триллион':10**12,
  'квадриллион':10**15,
  'квинтиллион':10**18,
  'секстиллион':10**21,
  'септиллион':10**24,
  'октиллион':10**27,
  'нониллион':10**30,
  'дециллион':10**33,
  'ундециллион':10**36,
}
SUMM=0
x=0
inp=[]
def convert(dict,a,b,a1,b1):
  for el in range(0,len(inp)):
    for k in range(0,len(list(dict.keys()))):
      try:
        if ( list(eval(a))[eval(a1)] in eval(b)[eval(b1)] and ( inp[el] != "девяносто" )):
          if ( 'сот' in inp[el] or 'сти' in inp[el] or 'сто' in inp[el]):

            if (inp[el] != 'сот' and inp[el] !='сти' and inp[el] !='сто' ):
              inp.insert(inp.index(inp[el]),inp[el][:-3])
              inp[el+1] = inp[el+1][-3:]
              break  
          inp[el]=list(dict.values())[k]
          break

        elif inp[el] == "девяносто":
          inp[el] = 90
          break
      except: break
  return inp

# list(eval(a))[inp] in eval(b)[k]
while inp!=["0"]:
  inp=input('Enter a your summ (not digits) or 0 to finish program: ').split(' ')
  inp=convert(KEY_WORD,"dict.keys()","inp","k","el")
  print(inp)
  inp=convert(DICT,"inp","dict.keys()","el","k")
  if inp!=["0"]:
    print(inp)
  
  # money= list(map(int,input('Enter a variants of money which i will give you (with tabs): ').split(" ")))


