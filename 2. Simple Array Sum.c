#include <math.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main()
{
int i,n;
scanf("%d",&n);
int a[n];
for(i=0; i<n; i++)
  { 
       scanf("%d", &a[i]);
  }
int sum=0;

for(i=0; i<n; i++)
   { 
    sum = sum + a[i];
   }
printf("%d", sum);
}
