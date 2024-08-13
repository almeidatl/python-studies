# criar um programa gerador de senhas
import random as r

def generate_password():
    # caracteres premitidos para a senha
    length = 12
    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    number = '0123456789'
    special = '!#$%&@*'
    # dicionário com as categorias de caracteres e quantidade necessária em cada senha
    categories = {
        'lowercase': (lowercase, 3),
        'uppercase': (uppercase, 3),
        'number': (number, 3),
        'special': (special, 3)
    }
    pass_characters = []
    while len(pass_characters) < length:
        for category, (character, count) in categories.items():
            required_characters = count
            if required_characters > 0:
                pass_characters.append(r.choice(character))
                required_characters -= 1
    r.shuffle(pass_characters)
    return ''.join(pass_characters)

password = generate_password()

print(f'**'*15)
print(f'Password created: {password}')
print(f'**'*15)
