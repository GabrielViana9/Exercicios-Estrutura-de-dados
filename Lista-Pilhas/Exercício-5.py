def inversamente(pilha:list):
    pilha_inversa = []

    for i in pilha[::-1]:
        pilha_inversa.append(i)

    return pilha_inversa

x = inversamente([1,2,3,4,5,6,7,8,9,10])
print(x)