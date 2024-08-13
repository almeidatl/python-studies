import random as r

lowercase = 'abcdefghijklmnopqrstuvwxyz'
uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
number = '0123456789'
special = '!#$%&@*'

length = 12
has_lowercase = 0
has_uppercase = 0
has_number = 0
has_special = 0

pass_caracteres = []

while len(pass_caracteres) < length:

    if has_lowercase < 3:
        pass_caracteres.append(r.choice(lowercase))
        has_lowercase += 1

    elif has_uppercase < 3:
        pass_caracteres.append(r.choice(uppercase))
        has_uppercase += 1

    elif has_number < 3:
        pass_caracteres.append(r.choice(number))
        has_number += 1

    elif has_special < 3:
        pass_caracteres.append(r.choice(special))
        has_special += 1

r.shuffle(pass_caracteres)

def FinalPass():
    password = ''.join(pass_caracteres)
    return password

print()
print(f'Senha gerada: {FinalPass()}')
print()