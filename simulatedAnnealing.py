import math,random

best = 0
t = 100000
x1 = 1
x2 = 1
alpha = 0.99

def randomState(a, b):
    x1 = a * random.uniform(-10, 10)
    x2 = b * random.uniform(-10, 10)
    if(-10 <= x1 <= 10 and -10 <= x2 <= 10):
        return x1, x2
    else:
        return randomState(a, b)

while (t > 0.01):
    a, b = randomState(x1, x2)
    hasil = - math.fabs( math.sin(a) * math.cos(b) * math.exp(math.fabs( 1 - ( math.sqrt( (a*a) + (b*b) ) / 3.14 ) ) ) )
    if best > hasil:
        x1 = a
        x2 = b
        best = hasil        
    elif(math.exp( (best - hasil) / t ) > random.random()):
        x1 = a
        x2 = b
        best = hasil
    print()
    print("Nilai X1: ",x1)
    print("Nilai X2: ",x2)
    print("Nilai minimum: ",best)
    t = alpha*t