alfabeto = "abcdefghijklmnopqrstuvxz"
vogais = {'a', 'e', 'i', 'o', 'u'}
vogal_cima = {}
vogal_baixo = {}
prox_consoante = {}
ult_vogal = None

palavra = input().lower()
nova_palavra = []


def add(posicao):
    for i in range(posicao + 1, len(alfabeto)):
        if alfabeto[i] in vogais:
            return i
    return posicao #caso não haja vogal para cima
    
def sub(posicao):
    for i in range(posicao -1, -1, -1):
        if alfabeto[i] in vogais:
            return i
    return posicao #caso não haja vogal para baixo

def consoante(posicao):
    for i in range(posicao + 1, len(alfabeto)):
        if alfabeto[i] not in vogais:
            return alfabeto[i]
    return posicao

    
for i in palavra:
    if i not in vogais and i in alfabeto:
        nova_palavra.append(i)
        p = alfabeto.index(i) #posição da consoante no alfabeto
        pmaior = add(p) 
        pmenor = sub(p)

        if pmaior - p < p - pmenor:
            nova_palavra.append(alfabeto[pmaior])
        elif pmaior - p == p - pmenor:
            nova_palavra.append(alfabeto[pmenor])
        else:
            nova_palavra.append(alfabeto[pmenor])

        nova_palavra.append(consoante(p))
    else:
        nova_palavra.append(i)


print("".join(nova_palavra))