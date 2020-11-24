import functions as fn


# генарация ключей двух пользователей по схеме Диффи-Хеллмана
print('\n\n  GENERATING KEYS : \n')

# пользователь A генерирует первым свой закрытый (a), открытый (A) ключ и числа p и g
# отправляет пользователю B свой открытый ключ и числа p и g
a, A, p, g = fn.generateKeys()
print('User A keys and numbers:')
print(' private key (a) : ', a)
print(' public key  (A) : ', A)
print(' numbers         : ', [p, g], '\n')

# пользователь B генерирует свои закрытый (b), открытый (B) и секретный (secretKeyForB) ключи на основании пришедшей информации от пользователя A
# отправляет пользователю A свой открытый ключ для того, чтобы он мог сгенерировать свой такой же секретный ключ (secretKeyForA)
b, B = fn.generateKeysBasedOnPrevious(p, g)
secretKeyForB = fn.generateSecretKey(b, A, p)
print('User B all keys:')
print(' private key (b) : ', b)
print(' public key  (B) : ', B)
print(' secret key      : ', secretKeyForB, '\n')

# пользователь A генерирует свой секретный ключ, который совпадает с секретным ключом пользователя B
secretKeyForA = fn.generateSecretKey(a, B, p)
print(' A`s secret key  : ', secretKeyForA)


# шифрование сообщения (text) пользователем A по схеме Эль-Гамаля
print('\n\n  SENDING AND READING THE MESSAGE : \n')

text = 'Hello, world!'
textArray = fn.textToArray(text)
print('Original message  : ', textArray, '\n')

encrypted = fn.encrypt(text, secretKeyForA, p)
print('Encrypted message : ', encrypted, '\n')

# отправка пары (открытый ключ, зашифрованное сообщение) пользователю B
sendData = (A, encrypted)

# расшифровка сообщения (encrypted) пользователем B
decrypted = fn.decrypt(sendData[0], sendData[1], b, p)
print('Decrypted message : ', decrypted)
