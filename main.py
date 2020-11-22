import functions as fn

# генерация ключей
p = fn.randPrime(16)
g = fn.primitiveRoot(p)

# p = 11
# g = 2

x = fn.genKey(p)
y = fn.power(g, x, p)

# x = 8
# y = 3

print('Ключи:\n', x, '\n', y, '\n\n')

# шифрование текста M
M = ord('w')
# M = 5

print(M)

k = fn.genKey(p)
# k = 9
a = fn.power(g, k, p)
b = fn.power(M * fn.power(y, k, p), 1, p)

print('Шифротекст:\n', a, '\n', b, '\n\n')

MD = fn.power(b * fn.power(a, p - 1 - x, p), 1, p)

print(MD)
