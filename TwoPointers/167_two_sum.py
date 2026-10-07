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


if __name__ == "__main__":
    numbers = [5,25,75]
    target = 100
    assert twoSum(numbers, target) == [2,3]


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