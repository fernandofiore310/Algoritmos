# Esperado antes: a abordagem vai ser via 2 ponteiros, com complexidade O(n)
# Tempo: 15min15s | Solução/vídeo consultado: não
# LeetCode: Primeira submissao deu o erro para uma lista de len=1. So coloquei a condicao no inicio e foi. 
# Complexidade esperada: O(n) | real: O(n)

# v3 - 20/10/26
# Tempo: 25min estourados
# Consulta: Nenhuma
# Resultado: Nao consegui acertar o exercicios novamente. OSSO!
# Complexidade esperada: O(n) | real: O(n), porem nao funcional

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

def remove_duplicates_v3(nums: List[int]) -> int:
    i1, i2 = 1, 1

    while i2 < len(nums):
        if nums[i2] != nums[i2-1]:
            i2 += 1
            i1 += 1
        else:
            while nums[i2] == nums[i2-1]:
                i2 += 1
            nums[i1] = nums[i2]
            i2 += 1
            i1 += 1

    return i1
            
# v4 - 27/10/26
# Tempo: 10min25s
# Consulta: Nenhuma
# Resultado: Bateu
# Complexidade esperada: O(n) | real: O(n)
# Fiz no papel e senti que me ajudou.

def remove_duplicates_v4(nums: List[int]) -> int:
    l, r = 1, 1

    while r < len(nums):
        if nums[l-1] == nums[r]:
            r += 1
        else:
            nums[l] = nums[r]
            l += 1
    return l

if __name__ == "__main__":
    lista = [1,2,4,4,4,5,6,6,7,7]
    lista2 = [1,1,2,3,5,5]
    lista3 = [0,0,0,0,0,0]
    lista4 = [1]
    assert remove_duplicates_v4(lista) == 6
    assert remove_duplicates_v4(lista2) == 4
    assert remove_duplicates_v4(lista3) == 1
    assert remove_duplicates_v4(lista4) == 1