# Tempo: feito em 22min
# Esperado: Do jeito que estou pensando aqui, acredito que vai ter que ser O(n), visto que vou ter que fazer tres lacos, um para percorrer s e montar o dic_s, outro igual para o dic_t, e outro para percorrer s e ver se as letras estao no dic_t
# Consulta: Nenhuma
# Conferencia: Passou no LeetCode, mas acredito que poderia ter feito melhor. Demorei nesse exercicio, pois queria ao maximo evitar usar o tres lacos. Mas nao consegui pensar em outra maneira, entao acabei fazendo. O codigo ficou em O(3n), que eh O(n).

def isAnagram(s, t):
    dic_s = {}
    dic_t = {}

    if len(s) != len(t):
        return False

    for l in s:
        if l not in dic_s:
            dic_s[l] = 1
        else:
            dic_s[l] += 1

    for c in t:
        if c not in dic_t:
            dic_t[c] = 1
        else:
            dic_t[c] += 1

    for l in s:
        if dic_t.get(l) == None:
            return False
        else:
            if dic_t.get(l) != dic_s.get(l):
                return False
    
    return True

# v2
# Tempo: 9min
# Esperado: O(n)
# Consulta: So perguntei ao Gemini como era feita a comparacao == entre dois dict em python
# Conferencia: Bateu, e o tempo de execucao foi melhor que o v1
# Consegui pensar em uma maneira pratica de fazer com o ==, sem precisar do terceiro laco.
# No entanto, nao consegui pensar em uma maneira de usar apenas um dicionario so. Se bem que imagino que seja possivel, porem nao sei se tao mais eficiente que a maneira que ja fiz.

def isAnagram_v2(s, t):

    dic_s = {}
    dic_t = {}

    for c in s:
        if c not in dic_s:
            dic_s[c] = 1
        else:
            dic_s[c] += 1

    for c in t:
        if c not in dic_t:
            dic_t[c] = 1
        else:
            dic_t[c] += 1

    return dic_s == dic_t

if __name__ == "__main__":
    s = "roma"
    t = "amor"
    s2 = "rat"
    t2 = "car"
    s3 = "anagram"
    t3 = "nagaram"
    assert isAnagram_v2(s, t) == True
    assert isAnagram_v2(s2, t2) == False
    assert isAnagram_v2(s3, t3) == True