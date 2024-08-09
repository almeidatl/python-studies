# criar um programa gerador de senhas

# o programa irá de forma aleatória escolher caracteres até que as condicoes de senha sejam atendidas

import random as r

lowercase = 'abcdefghijklmnopqrstuvwxyz'
uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
number = '0123456789'
special = '!#$%&@*'

# define as condicoes de senha

length = 12
has_lowercase = 0
has_uppercase = 0
has_number = 0
has_special = 0

pass_caracteres = []

for lower in lowercase:
    
    if has_lowercase < 3:
        pass_caracteres.append(r.choice(lowercase))
        has_lowercase += 1

for upper in uppercase:
    
    if has_uppercase < 3:
        pass_caracteres.append(r.choice(uppercase))
        has_uppercase += 1

for num in number:
    
    if has_number < 3:
        pass_caracteres.append(r.choice(number))
        has_number += 1

for spec in special:
    
    if has_special < 3:
        pass_caracteres.append(r.choice(special))
        has_special += 1

# print(pass_caracteres)
r.shuffle(pass_caracteres)

def FinalPass():
    password = ''
    for i in pass_caracteres:
        password += i
    return password

print(f'Senha: {FinalPass()}')