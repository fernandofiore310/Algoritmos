# v1 - 20/10/26
# Tempo: 25 min estourados
# Consulta: Video NeetCode
# Resultado: Estava fazendo a solucao certa, mas sem querer, fiz em cima da original, entao desfiz.
# Complexidade esperada: 
# “Já vi isso antes?”	set	    os elementos vistos
# “Quantas vezes vi?”	dict	elemento → contagem
# “Onde vi?”	        dict	elemento → índice
# “Quem é parecido com quem?”	dict	característica comum → lista de elementos

def topKFrequent(nums, k):
    dic = {}

    for n in nums:
        if n not in dic:
            dic[n] = 1
        else:
            dic[n] += 1

    l = []
    i = 0
    while i < k:
        maior_v = 0
        maior_c = 0
        for c, v in dic.items():
            if v > maior_v and c not in l:
                maior_c = c
                maior_v = v
        l.append(maior_c)
        i += 1

    print(l)
    return l

if __name__ == "__main__":
    lista = [1,2,4,4,4,5,6,6,7,7]
    assert topKFrequent(lista, 2) == [4, 6]