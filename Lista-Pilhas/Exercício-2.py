def pilhas_iguais(listaPilhas1:list,listaPilhas2:list):
    if listaPilhas1 == listaPilhas2:
        return True
    else:
        return False

x = pilhas_iguais([1,2,3],[1,2,3])
z = pilhas_iguais([1,2,3],[3,2,1])

print("Essa lista de pilhas é:", x)
print("Essa lista de pilhas é:", z)