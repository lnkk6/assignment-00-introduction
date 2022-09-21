import math
a = list(map(int, input().split()))


#print(a)

#print(math.sin(10))

#print(min(a), max(a), sum(a), sum(a)/len(a))

#s = 'gfomjvf'
#for c in s:
    #print(c)

print(f'Hello, {a:.5f}!')

s=input('what is your name? ')
print(f'Hello, {s}! Nice to meet you!')

for item in a:
    print(item)

    divisors = []
    for i in range (2, item + 1):
        if item % i == 0:
            divisors.append(i)
    print(divisors)


    primes = []
    for i in range (2, int(item**0.5)+1):
        while item % i == 0:
            primes.append(i)
            item = item // i
    if item > 1:
        primes.append(item)
    print(primes)