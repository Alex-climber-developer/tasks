a=str(input("Введите целое неотриц. число  "))
dec=a[-2:-1]
print(dec)


count=int(input("кол-во уроков  "))
finish_time=count*45+(count//2)*5+((count-1)//2)*15
timechas=finish_time//60
timemin=finish_time-(timechas*60)
print((timechas+9), timemin, sep=" ")
