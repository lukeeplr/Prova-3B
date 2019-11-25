def questao2():
    containers = ['c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'c9', 'c10', 'c11', 'c12']

    porto = {
        'p1': Pilha(5),
        'p2': Pilha(5),
        'p3': Pilha(5),
        'p4': Pilha(5),
        'swap': Pilha(5)
    }
    p = 1
    for x in containers:
        if p > 4: p = 1
        porto['p' + str(p)].push(x)
        p += 1

    remover = ['c1', 'c6', 'c8']

    for contain in remover:
        for pilha in porto.values():
            if pilha.found(contain):
                aux = pilha.items[pilha.top - 1]
                if aux == contain:
                    pilha.pop()
                else:
                    while aux != contain: 
                        aux = pilha.pop()
                        if aux != contain: porto['swap'].push(aux)
                    while not porto['swap'].empty():
                        cont = porto['swap'].pop()
                        pilha.push(cont)
                break

    for k, v in porto.items():
        print('-=-')
        print(k+':')
        print()
        v.show()
        print('-=-')


questao2()
