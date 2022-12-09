
sqr = int(input("Your number:"))
x = 0
i = 1
e = 0

while x * x != sqr:
    e += 1
    while (x+i) * (x+i) <= sqr:
        x += i
        if e >= 17:
            break
    if e >= 17:
        break
    i /= 10

xPlusQuadrillionth = x + 0.000000000000001

if x * x != sqr:
    print(f"Your number is in-between {x} and {xPlusQuadrillionth} ")
            
elif x * x == sqr:
    print(f"The square root of {sqr} is {x}")
    
else:
    print("An error occurred because the code is a piece of shit")
    
#10.583005244258361    
#0.000000000000001
#Quadrillionth