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
    lista_retorno = []
    if len(nums) == 1:
        return nums
    
    i1 = 0
    i2 = 1
    k = 0

    while True:
        n1 = nums[i1]
        n2 = nums[i2]

        

if __name__ == "__main__":
    lista = [1,2,3,4,4,5,6,6,6,7]
    lista2 = ['G', 'P', 'T']
    assert remove_duplicates(lista) == 7
    # assert inverte_string(lista2) == ['T', 'P', 'G']


# Tempo: 15min15s | Solução/vídeo consultado: não
# LeetCode: Primeira submissao deu o erro para uma lista de len=1. So coloquei a condicao no inicio e foi. 
# Complexidade esperada: O(n) | real: O(n)