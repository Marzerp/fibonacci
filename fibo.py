#!usr/bin/env python3
#by Marzerp
#LICENSE GNU/GPL
#My first sequence

#sumar los 10 primeros numeros enteros

n=10
a=1
b=1
print(a)
print(b)
fibo.append(a)
fibo.append(b)
for x in range(n+1):
    print(a+b)
    c=a+b
    #print(c)
    fibo.append(c)
    a=b
    b=c

print(fibo)

for i in range(len(fibo-1)):
    print(fibo[i]/fibo[i+1])
    
gold_ratio = fibo[-i]/fibo[-i-1]  
    
