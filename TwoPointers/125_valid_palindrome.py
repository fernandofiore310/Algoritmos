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

if __name__ == "__main__":
    s = "A man, a plan, a canal: Panama"
    s2 = "Fernando !"
    assert isPalindrome(s) == True
    assert isPalindrome(s2) == False


# Tempo: 18min14s | Solução/vídeo consultado: não
# LeetCode: Nao foi aceito nas primeiras, pois estava usando uma lista para os caracteres nao especiais. Entao achei essa funcao na internet e apliquei. Ai nao foi de novo, mas foi por que esqueci do " ". Arrumei isso e deu certo. 
# Complexidade esperada: O(n) | real: O(n)