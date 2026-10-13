# Esperado antes: a abordagem vai ser via 2 ponteiros, com complexidade O(n)

from typing import List

def remove_duplicates(nums: List[int]) -> int:

    if len(nums) == 1:
        return 1
    
    i1 = 0
    i2 = 1

    while True:
        if nums[i1] != nums[i2]:
            i1 += 1
            i2 += 1

        else:
            del nums[i2]

        if i2 > len(nums)-1:
            break

    return len(nums)

def remove_duplicates_v2(nums: List[int]) -> int:
    # A lista esta ordenada, logo, se um numero esta repetido, sua copia esta a sua direita.
    # Nesse codigo, tive problema com os ultimos numeros da lista, principalmente quando sao repetidos
    # Alem disso, coloquei um loop dentro do outro, mas acredito que esse esquema nao altera a complexidade O(n) dele.
    i1, i2 = 1 , 1

    while i2 < len(nums):
        if nums[i2] != nums[i2-1]:
            nums[i1] = nums[i2]
            i1 += 1
            i2 += 1
        else:
            i2 += 1

    return i1

if __name__ == "__main__":
    lista = [1,2,4,4,4,5,6,6,7,7]
    lista2 = [1]
    lista3 = [0,0,0,0,0,0]
    assert remove_duplicates_v2(lista) == 6
    assert remove_duplicates_v2(lista2) == 1
    assert remove_duplicates_v2(lista3) == 1


# Tempo: 15min15s | Solução/vídeo consultado: não
# LeetCode: Primeira submissao deu o erro para uma lista de len=1. So coloquei a condicao no inicio e foi. 
# Complexidade esperada: O(n) | real: O(n)