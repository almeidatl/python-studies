# criar um programa gerador de senhas
import random as r

class Generator:
    def __init__(self, length, required):
        self.required = required
        self.length = length

    def generate_password(self):
        # caracteres premitidos para a senha
        lowercase = 'abcdefghijklmnopqrstuvwxyz'
        uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        number = '0123456789'
        special = '!#$%&@*'
        # dicionário com as categorias de caracteres e quantidade necessária em cada senha
        categories = {
            'lowercase': (lowercase, self.required),
            'uppercase': (uppercase, self.required),
            'number': (number, self.required),
            'special': (special, self.required),
        }
        pass_characters = []
        while len(pass_characters) < self.length:
            for category, (character, count) in categories.items():
                required_characters = count
                if required_characters > 0:
                    pass_characters.append(r.choice(character))
                    required_characters -= 1
        r.shuffle(pass_characters)
        return ''.join(pass_characters)

# instancia para criar uma senha de 12 digitos com 3 caracteres de cada tipo
password12 = Generator(12, 3).generate_password()
# instancia para criar uma senha de 24 digitos com 6 caracteres de cada tipo
password24 = Generator(24, 6).generate_password()
# instancia para criar uma senha de 50 digitos com 3 caracteres de cada tipo
password50 = Generator(50, 10).generate_password()

print(f'**'*30)
print(f'Password 12 characters: {password12}')
print(f'**'*30)
