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