# 27. Uma lista  s diz-se sufixo de uma lista  w se  s for um segmento do fim de  w Defina a função 
# sufixoQ que recebe como argumentos duas listas  s e  w e devolve True se  s for sufixo de  w e False em 
# caso contrário.


def sufixoQ(l1=[], l2=[], pos=0, posneg=0,r=True):
    if posneg == 0:
        posneg = len(l1) * -1
            
    if pos == len(l1):
        return r
    if len(l1) > len(l2):       
        return r == False


    if l1[pos] == l2[posneg]:
        r = True
        pos += 1
        posneg += 1

    else:
        r = False
        return r

    return sufixoQ(l1,l2,pos,posneg,r)




print(sufixoQ([3,4],[1,2,3,4]))
print(sufixoQ([3,4],[1,2,3,4,5]))
print(sufixoQ([1,2,3],[1,2]))
print(sufixoQ([],[1]))
print(sufixoQ([1,2,3],[1,2,3]))

# saída
# True
# False
# False
# True
# True