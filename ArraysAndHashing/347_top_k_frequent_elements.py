# v1 - 20/10/26
# Tempo: 25 min estourados
# Consulta: Video NeetCode
# Resultado: Estava fazendo a solucao certa, mas sem querer, fiz em cima da original, entao desfiz.
# Complexidade esperada: | real: O(n+m*k) onde n = len(numms); m = numero de chaves de dic; e k 
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

# v2 - 27/10/26
# Tempo: 25 min estourados
# Consulta: Video NeetCode
# Resultado: Tentei implementar a solucao do cara do video. A lista ficou certa, no entanto, na hora de pegar a lista final, deu algum erro com o pop
# Complexidade esperada: | real: O(n+d+d) sendo n o len de nums e d o numero de elementos unicos em nums.
# “Já vi isso antes?”	set	    os elementos vistos
# “Quantas vezes vi?”	dict	elemento → contagem
# “Onde vi?”	        dict	elemento → índice
# “Quem é parecido com quem?”	dict	característica comum → lista de elementos

def topKFrequent_v2(nums, k):
    d = {}
    l = [0] * len(nums)

    for n in nums:
        if n not in d:
            d[n] = 1
        else:
            d[n] += 1
    
    print(d)

    for k, v in d.items():
        if l[v] == 0:
            l[v] = [k]
        else:
            l[v].append(k)
    
    print(l)

    lr = []
    i = len(l)-1
    while i > 0:
        if k > 0:
            if l[i] == 0 or (l[i] is list and len(l[i]) == 0):
                i -= 1
            else:
                n = l[i].pop()
                lr.append(n)
                k -= 1
        else:
            break

    print(lr)
    return lr 

if __name__ == "__main__":
    lista = [1,2,4,4,4,5,6,6,7,7]
    assert topKFrequent_v2(lista, 2) == [4, 6]