# Tempo: Versao 1 feita em 24min e versao 2 feita em 15min
# Esperado: Imagino que nao de para usar dois ponteiros nesse exercicio, pois a lista nums nao esta ordenada. Vou tentar fazer em um O(n) ao inves de fazer o O(n^2) convencional
# Consulta: Nenhuma na versao 1 e na segunda vi o video do LeetCode.
# Conferencia: Passou no LeetCode, mas com um tempo horrivel. Eu fiquei grande parte do tempo pensando em uma solucao O(n) e nao consegui, entao para nao deixar incompleto, escrevi o jeito O(n^2) que eu sabia.
# Explicação: Esse problema requer que a funcao devolva o indice de ambos os numeros. Nesse caso, a pergunta que ele responde eh "Onde vi?".
# A complexidade da primeira versao ficou em O(n^2) e a segunda em O(n) (O(2n) considerando que montamos um hashmap/dict).


def twoSum(nums, target):
    for i, n in enumerate(nums):
        for c, l in enumerate(nums):
            if i != c:
                if n + l == target:
                    return [i, c]

def twoSum_v2(nums, target):
    dic = {}

    for i, n in enumerate(nums):
        dif = target-n
        if dif not in dic:
            dic[n] = i
        else:
            return [dic[dif], i]

# v3 - 27/10/26
# Tempo: 15 min estourados
# Consulta: Nenhuma
# Resultado: Tentei fazer de cabeca, achei que tinha chegado em algum lugar, mas pelo jeito nao deu em nada.
# Complexidade esperada: | real: O(n+n) sendo n o len de nums
# “Já vi isso antes?”	set	    os elementos vistos
# “Quantas vezes vi?”	dict	elemento → contagem
# “Onde vi?”	        dict	elemento → índice
# “Quem é parecido com quem?”	dict	característica comum → lista de elementos

def twoSum_v3(nums, target):
    d = {}
    
    for i, n in enumerate(nums):
        d[n] = i
    
    print(d)

    for i, n in enumerate(nums):
        diff = target - n
        if diff in d:
            if d[diff] > i:
                return [i, d[diff]]
            else:
                return [d[diff], i]

if __name__ == "__main__":
    nums = [3, 2, 4]
    target = 6
    assert twoSum_v3(nums, target) == [1, 2]

    nums2 = [-1, -3, -2]
    target2 = -3
    assert twoSum_v3(nums2, target2) == [0, 2]

    nums3 = [7, 1, 7]
    target3 = 14
    assert twoSum_v3(nums3, target3) == [0, 2]