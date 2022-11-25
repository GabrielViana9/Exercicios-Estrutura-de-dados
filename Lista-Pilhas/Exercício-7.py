def TPilha2(N:list,P:list,vetor:list):
    for i in range(len(vetor)):
        if vetor[i] == 0:
            if len(N) > 0:
                N.pop()
            if len(P) > 0:
                P.pop()

        elif vetor[i] > 0:
            P.append(vetor[i])

        else:
            N.append(vetor[i])

    print("Números Negativos:", N,"Números Positivos:", P)

x = TPilha2([],[],[0,-1,1,-2,2])