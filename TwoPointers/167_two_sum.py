# Esperado antes: a abordagem vai ser via 2 ponteiros, com complexidade O(n)

from typing import List

def twoSum(numbers: List[int], target: int) -> List[int]:
    index1 = 0
    index2 = len(numbers)-1

    while True:

        if numbers[index1] + numbers[index2] == target:
            return [index1+1, index2+1]

        elif numbers[index1] + numbers[index2] < target:
            index1 += 1

        else:
            index2 -= 1

def twoSum_v2(numbers: List[int], target: int) -> List[int]:
    index1 = 0
    index2 = len(numbers)-1

    while True:
        s = numbers[index1] + numbers[index2]

        if s == target:
            return [index1+1, index2+1]
        elif s < target:
            index1+=1
        else:
            index2-=1

# v3 - 26/10/26
# Tempo: 10min
# Consulta: Nenhuma
# Resultado: Nao bateu, deu erro em casos que se tem numeros negativos e positivos na mesma lista
# Complexidade esperada: O(n)

def twoSum_v3(numbers: List[int], target: int) -> List[int]:
    l = 0
    r = len(numbers)-1

    while l < r:
        soma = abs(numbers[r]+numbers[l])
        if soma > abs(target):
            r-=1
        elif soma < abs(target):
            l+=1
        else:
            return [l+1, r+1]

if __name__ == "__main__":
    numbers = [1, 4, 5, 7, 8, 13]
    target = 12
    numbers2 = [-2, -5, -8, -12]
    target2 = -13
    numbers3 = [-2, -5, -8, -12]
    target3 = -14
    assert twoSum_v3(numbers, target) == [2,5]
    assert twoSum_v3(numbers2, target2) == [2,3]
    assert twoSum_v3(numbers3, target3) == [1,4]


# Tempo: 25min estourados | Solução/vídeo consultado: sim, mas so vi o raciocinio dele, nao vi ele escrevendo o codigo. Escrevi a solucao de cabeca.
# LeetCode: Minhas duas primeiras tentativas nao foram aceitas, a primeira por tempo e a segunda por indice2 maior que len. Em ambas estava usando um indice no primeiro elemento, e o segundo percorrendo o resto. Depois, vendo o video, me liguei que era melhor usar esq e dir. 
# Complexidade esperada: O(n) | real: O(n)

#Tentativa 1
# def twoSum(numbers: List[int], target: int) -> List[int]:
#     index1 = 0
#     index2 = 1
#     i = 0

#     while True:

#         if index2 == len(numbers):
#             index1 += 1
#             index2 = index1+1

#         if numbers[index1] + numbers[index2] == target:
#             print(i)
#             return [index1+1, index2+1]

#         else:
#             index2 += 1

#Tentativa 2
# def twoSum(numbers: List[int], target: int) -> List[int]:
#     index1 = 0
#     index2 = 1
#     i = 0

#     while True:

#         if numbers[index1] + numbers[index2] == target:
#             print(i)
#             return [index1+1, index2+1]

#         elif numbers[index1] + numbers[index2] < target:
#             index2 += 1

#         else:
#             index1 += 1
#             index2 = index1+1

