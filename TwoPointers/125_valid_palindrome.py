# Esperado antes: a abordagem vai ser via 2 ponteiros, com complexidade O(n)

import string

def isPalindrome(s : str) -> bool:
    s = s.lower()
    l = string.punctuation

    for c in s:
        if c in l or c == " ":
            s = s.replace(c, "")

    esq = 0
    dirr = len(s)-1

    while True:
        if esq > dirr:
            break

        if s[esq] != s[dirr]:
            return False

        else:
            esq +=1
            dirr -=1

    return True

def isPalindrome_v2(s : str) -> bool:
    i1 = 0
    i2 = len(s)-1

    p = s.lower()
    
    while i1 < i2:
        if p[i1].isalnum() and p[i2].isalnum():
            if p[i1] == p[i2]:
                i1 += 1
                i2 -= 1
            else:
                return False
        elif not p[i1].isalnum():
            i1+=1
        elif not p[i2].isalnum():
            i2-=1
        else:
            i1 += 1
            i2 -= 1
    return True

# v3 - 26/10/26
# Tempo: 10min
# Consulta: Nenhuma
# Resultado: Bateu.
# Complexidade esperada: O(n)

def isPalindrome_v3(s : str) -> bool:
    s = s.lower()
    l = 0
    r = len(s)-1

    while l < r:
        if s[l].isalnum() and s[r].isalnum():
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return False
        elif not s[l].isalnum():
            l += 1
        elif not s[r].isalnum():
            r -= 1
    return True

if __name__ == "__main__":
    s = "A man, a plan, a canal: Panama"
    s2 = "Fernando !"
    assert isPalindrome_v3(s) == True
    assert isPalindrome_v3(s2) == False


# Tempo: 18min14s | Solução/vídeo consultado: não
# LeetCode: Nao foi aceito nas primeiras, pois estava usando uma lista para os caracteres nao especiais. Entao achei essa funcao na internet e apliquei. Ai nao foi de novo, mas foi por que esqueci do " ". Arrumei isso e deu certo. 
# Complexidade esperada: O(n) | real: O(n)