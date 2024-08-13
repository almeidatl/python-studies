'''
comparar dois arrays (ou listas) de inteiros, a e b, que têm o mesmo tamanho. A comparação entre a e b ocorre elemento por elemento, e você deve somar pontos para cada elemento com base nas seguintes regras:

Se o elemento a[i] for maior que b[i], então a recebe 1 ponto.
Se o elemento b[i] for maior que a[i], então b recebe 1 ponto.
Se a[i] for igual a b[i], nenhum dos dois recebe pontos.
A função deve retornar uma lista com dois inteiros: o primeiro inteiro representa os pontos de a, e o segundo representa os pontos de b.
'''


class CompareTriplets:

    def __init__(self):
        pass

    def compare():
        # iniciar listas
        a = []
        b = []

        score_a = 0
        score_b = 0

        # adiciona os pontos nas listas
        for i in range(1, 4):
            a.append(int(input(f'{i}º rount points: ')))
            b.append(int(input(f'{i}º rount points: ')))

        for valor_a, valor_b in zip(a, b):

            if valor_a > valor_b:
                score_a += 1
            elif valor_b > valor_a:
                score_b += 1
            elif valor_a == valor_b:
                pass

        return score_a, score_b


print(CompareTriplets.compare())
