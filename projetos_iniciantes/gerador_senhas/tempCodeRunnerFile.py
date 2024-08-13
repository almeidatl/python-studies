# caracteres premitidos para a senha
    length = 12
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
    while len(pass_characters) < length:
        for category, (character, count) in categories.items():
            required_characters = count
            if required_characters > 0:
                pass_characters.append(r.choice(character))
                required_characters -= 1
    r.shuffle(pass_characters)
    return ''.join(pass_characters)