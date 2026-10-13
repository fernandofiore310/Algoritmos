# Tempo: feito em 8min1s
# Esperado: O codigo vai ser no maximo O(n), pois vou precisar percorrer os elementos da lista
# Consulta: Consultei na internet como adiciona um valor a um set
# Conferencia: Passou no LeetCode, e sim, ele tem que ser O(n) pois vai ser necessario eventualmente percorrer pelo menos parte do array


def containsDuplicate(nums):
    s = set()

    for n in nums:
        if n not in s:
            s.add(n)
        else:
            return True
    return False

if __name__ == "__main__":
    lista = [1,2,3,1]
    lista2 = [1,2,3,4,5,6,7,8,9,0]
    lista3 = [0]
    assert containsDuplicate(lista) == True
    assert containsDuplicate(lista2) == False
    assert containsDuplicate(lista3) == False