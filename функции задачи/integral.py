sh=0.1
start=0
end=1
upprox=0.001
S= 0

while start<= end:
  f= 2**(3*start)
  s_i=sh*f
  S+=s_i
  start+=sh
  
print(round(S,3))