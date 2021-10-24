// без
#include <stdlib.h>
#include <stdio.h>
#include <float.h> 
#include <math.h>  

int main() {
  char inc=1;
  int n = 0, fact=1;
  float summ=0, prev_summ = 0, e= 0.0000001, diff=0; 
  do {
    prev_summ=summ;
    summ+= inc*(pow((M_PI/3),2*n+1)/fact);
    diff = fabs(prev_summ - summ);
    inc*=-1;
    fact*=(2*++n+1)*2*n;
  } while(diff > e) ;
  printf("%f\n",summ);
  return 0;
}

// с рекурентными функциями 
#include <stdlib.h>
#include <stdio.h>
#include <float.h> 
#include <math.h>  

int main() {
  double a=M_PI/3, s0= 0,s1=a, e= 0.0000001,n=1;
  while(fabs(s1-s0) > e) {
    s0=s1;
    a*=-(M_PI/3)*(M_PI/3)/(2*n*(2*n+1));
    n++;
    s1+=a;
  } 
  printf("%lf\n",s1);
  return 0;
}