# v1 - 20/10/26
# Tempo: 25min estourados. COm 15 minutos, desisti e fui para os videos.
# Consulta: Vi dois videos, vi a explicacao do primeiro e nao entendi. A do segundo eu ate entendi, mas nao cheguei perto de pensar nisso.
# Resultado: Nao consegui resolver.
# Complexidade esperada: nao sei.
# “Já vi isso antes?”	set	    os elementos vistos
# “Quantas vezes vi?”	dict	elemento → contagem
# “Onde vi?”	        dict	elemento → índice
# “Quem é parecido com quem?”	dict	característica comum → lista de elementos

def groupAnagrams(strs):
    dic = {}

    for s in strs:
        if s not in dic:
            dic[s] = {}
            for c in s:
                if c not in dic[s]:
                    dic[s][c] = 1
                else:
                    dic[s][c] += 1

# v2 - 27/10/26
# Tempo: Tentei por 6 minutos, nao consegui e fui para o video. Vi o video, tentei implementar do meu jeito e nao foi.
# Consulta: Video do NeetCode
# Resultado: Nao consegui resolver.
# Complexidade esperada: era pra ser O(m*n) sendo n o tamanho de cada string e m o tamanho da lista
# “Já vi isso antes?”	set	    os elementos vistos
# “Quantas vezes vi?”	dict	elemento → contagem
# “Onde vi?”	        dict	elemento → índice
# “Quem é parecido com quem?”	dict	característica comum → lista de elementos

def groupAnagrams_v2(strs):
    d = {}

    for s in strs:
        d2 = {}
        
        for c in s:
            if c not in d2:
                d2[c] = 1
            else:
                d2[c] += 1
        
        if tuple(d2) not in d:
            d[tuple(d2)] = [s]
        else:
            d[tuple(d2)].append(s)

    print(d)

    l = []
    for ls in d.values():
        l.append(ls)

    return l

if __name__ == "__main__":
    s = ["eat","tea","tan","ate","nat","bat"]
    s2 = [""]
    s3 = ["a"]
    assert groupAnagrams_v2(s) == [["bat"],["nat","tan"],["ate","eat","tea"]]
    assert groupAnagrams_v2(s2) == [[""]]
    assert groupAnagrams_v2(s3) == [["a"]]