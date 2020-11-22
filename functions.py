import random
import math
import sys
sys.setrecursionlimit(1500)

# быстрый поиск модуля от степени числа
def power(x, n, mod):
    if n == 0:
        return 1
    elif n % 2 == 0:
        p = power(x, n / 2, mod)
        return (p * p) % mod
    else:
        return (x * power(x, n - 1, mod)) % mod

# генерация случайного числа фиксированной длины
def rand(n):
    rangeStart = 10 ** (n-1)
    rangeEnd = (10 ** n) - 1
    return random.randint(rangeStart, rangeEnd)

# определение простое ли число
def isPrime(num):
    if (num < 2):
        return False
    for prime in LOW_PRIMES:
        if (num == prime):
            return True
        if (num % prime == 0):
            return False
    return MillerRabin(num)

# решето Эратосфена
def primeSieve(sieveSize):
    sieve = [True] * sieveSize
    sieve[0] = False # Zero and one are not prime numbers.
    sieve[1] = False
    for i in range(2, int(math.sqrt(sieveSize)) + 1):
        pointer = i * 2
        while pointer < sieveSize:
            sieve[pointer] = False
            pointer += i
    primes = []
    for i in range(sieveSize):
        if sieve[i] == True:
            primes.append(i)
    return primes

# тест Миллера-Рабина
def MillerRabin(num):
    if num % 2 == 0 or num < 2:
        return False
    if num == 3:
        return True
    s = num - 1
    t = 0
    while s % 2 == 0:
        s = s // 2
        t += 1
    for trials in range(5):
        a = random.randrange(2, num - 1)
        v = pow(a, s, num)
        if v != 1:
            i = 0
            while v != (num - 1):
                if i == t - 1:
                    return False
                else:
                    i = i + 1
                    v = (v ** 2) % num
    return True

# генерация большого простого числа
def randPrime(n):
    rangeStart = 10 ** (n-1)
    rangeEnd = (10 ** n) - 1
    while True:
        num = random.randint(rangeStart, rangeEnd)
        if isPrime(num) and str(num)[-1] != '6' and str(num)[-1] != '1':
            return num

# вычисление функции Эйлера
def EulersFunction(num):
    e = num
    arr = [[num]]
    for i in arr:
        e *= (i[0] - 1) / i[0]
    return int(e)

# нахождение делителей числа
def divisors(num):
    arr = []
    arr2 = []
    d = 2
    while len(arr2) != 1:
        if num % d == 0:
            num /= d
            arr2 += [d]
        else:
            if len(arr2) != 0:
                arr.append(arr2)
                arr2 = []
            d += 1
    arr.append(arr2)
    return arr

# нахождение первообразного корня для от числа p
def primitiveRoot(num):
    if isPrime(num):
        e = EulersFunction(num)
        arrDivisors = divisors(e)
        arrAnswers = []
        for i in range(2, num):
            arrMiddleAnswers = []
            for j in range(0, len(arrDivisors)):
                arrMiddleAnswers.append(power(i, int(e / arrDivisors[j][0]), num))
            if 1 not in arrMiddleAnswers:
                arrAnswers.append(i)
            if len(arrAnswers) == 10:
                break
        return arrAnswers[0]
    else:
        raise Exception('Impossible to decide')

LOW_PRIMES = primeSieve(100)

def gcd(a, b):
    if a < b:
        return gcd(b, a)
    elif a % b == 0:
        return b;
    else:
        return gcd(b, a % b)

def genKey(p):
    key = rand(len(str(p)) - 1)
    while gcd(p, key) != 1:
        key = rand(len(str(p)) - 1)
    return key
