t1 = int(0)
t2 = int(1)
t3 = int(0)

value = 34

while value > t3:
    t3 = t1 + t2
    t1 = t2
    t2 = t3

if value == 0 or value == 1:
    print ('O numero faz parte da sequencia de Fibonacci.')

elif value == t3:
    print ('O numero faz parte da sequencia de Fibonacci.')

else:
    print ('O numero digitado nao faz parte da sequencia de Fibonacci.')
       