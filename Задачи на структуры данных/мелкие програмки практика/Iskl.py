	
ch_1=input("Введите 1 число: ")
ch_2=input("Введите 2 число: ")
try:
   ch_1=int( ch_1)
   ch_2=int( ch_2)
except (ValueError, TypeError) : 

   print(str(ch_1+ch_2))

else:
   print(ch_1+ch_2)