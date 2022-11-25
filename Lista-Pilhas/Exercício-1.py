def elemento_maior(pilha):
    maiorNum = pilha[0]
    for i in range(len(pilha)):
        if pilha[i] > maiorNum:
            maiorNum = pilha[i]
    return maiorNum

p = elemento_maior([1,2,9,7,4])

print(p)