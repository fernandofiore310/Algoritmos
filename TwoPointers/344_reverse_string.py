# Por que dois ponteiros é O(n)?
# Dois ponteiros é O(n) pois, no pior cenário possível, por exemplo em uma lista de 10 elementos, é apenas um dos ponteiros andarem, o que nesse caso, significa que ele vai ter percorrido a lista toda para encontrar o outro ponteiro.
# O mesmo caso vale para caso eu ande um ponteiro de cada vez, visto que, no pior caso, precisariam de nove passos para ficar um do lado do outro, e mais um de algum ponteiro para ficarem na mesma casa, totalizando 10 passos.
# Em uma lista com 10000 elementos, o pior caso contaria com 10000 passos.

# Esperado antes: a abordagem vai ser via 2 ponteiros, com complexidade O(n)

from typing import List

def inverte_string(lista: List) -> List:
    esq = 0
    dirr = len(lista)-1

    while True:
        if esq > dirr:
            break

        e1 = lista[esq]
        e2 = lista[dirr]
        lista[esq] = e2
        lista[dirr] = e1
        
        esq += 1
        dirr -= 1
    
    return lista

if __name__ == "__main__":
    lista = ['C', 'l', 'a', 'u', 'd', 'e']
    lista2 = ['G', 'P', 'T']
    assert inverte_string(lista) == ['e', 'd', 'u', 'a', 'l', 'C']
    assert inverte_string(lista2) == ['T', 'P', 'G']


# Tempo: 15min | Solução/vídeo consultado: não
# LeetCode: Accepted na primeira submissão 
# Complexidade esperada: O(n) | real: O(n)