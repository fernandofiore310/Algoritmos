# Tempo: feito em 24min
# Esperado: Imagino que nao de para usar dois ponteiros nesse exercicio, pois a lista nums nao esta ordenada. Vou tentar fazer em um O(n) ao inves de fazer o O(n^2) convencional
# Consulta: Nenhuma
# Conferencia: Passou no LeetCode, mas com um tempo horrivel. Eu fiquei grande parte do tempo pensando em uma solucao O(n) e nao consegui, entao para nao deixar incompleto, escrevi o jeito O(n^2) que eu sabia.


def twoSum(nums, target):

    for i, n in enumerate(nums):
        for c, l in enumerate(nums):
            if i != c:
                if n + l == target:
                    return [i, c]


if __name__ == "__main__":
    nums = [2, 5, 4, 8, 9, 0]
    target = 5
    assert twoSum(nums, target) == [1, 5]