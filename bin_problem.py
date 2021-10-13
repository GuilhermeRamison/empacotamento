from Box import *
from Packer import *
from Item import *


def best_choice():
    all_items_fitted = False
    for box in packer.boxes:
        if len(box.unfitted_items) == 0:
            all_items_fitted = True
            print(f'Melhor opção para o seu Manoel: {box.name}')
            break
    if not all_items_fitted:
        print('Será necessário mais de uma caixa para empacotar a lista de itens.')


def build_packs(pack_box):
    raw_packs = pack_box.split('\n\n')
    return [raw_pack for raw_pack in raw_packs]


test1 = '40 10 25\n40 30 30\n15 20 10\n10 30 10\n30 15 10'
test2 = '10 15 30\n20 10 20\n\n10 10 10\n20 20 20\n30 10 10'
test3 = '10 15 30\n20 10 20\n\n10 10 10\n20 20 20\n30 10 10\n50 80 60\n40 30 30\n15 20 10\n10 30 10\n30 15 10'

packs = build_packs(test3) # selecionar a lista de teste
for pack in packs:
    packer = Packer()
    units = [u.split(' ') for u in pack.split('\n')]
    items = [Item(b[0], b[1], b[2]) for b in units]
    for item in items:
        packer.add_item(item)
    packer.add_box(Box('Caixa 1', 30, 40, 80))
    packer.add_box(Box('Caixa 2', 80, 50, 40))
    packer.add_box(Box('Caixa 3', 50, 80, 60))
    packer.pack()
    '''packer.print_boxes()''' # Printar como fica a lista de itens nas 3 caixas
    print(f'Pack número {packs.index(pack)}')
    best_choice()


# Explicação:
'''Pensei em testar todas as possibilidades de colocar as caixas menores na caixa grande.
Para testar todos os casos, eu iria aninhar muitos for's resultando em uma complexidade
exponencial, deixando o seu Manoel esperando muito tempo dependendo da entrada do 
programa. 
    Então, pesquisei e vi que se trata do problema do empacotameto (bin packing problem),
    onde já foram estudadas algumas heurísticas para deixar o algoritmo viável no quesito
    de tempo computacional (em comparação com a minha ideia inicial).
    Depois de ver algumas heurísticas, eu iria pegar a ideia do algoritmo fisrt-fit, onde 
    colocamos sempre as maiores caixas primeiro'''