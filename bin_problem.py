'''class Box:
    def __init__(self, height, width, depth):
        self.height = int(height)
        self.width = int(width)
        self.depth = int(depth)
        self.swap_num = 0


def build_packs(pack_box):
    raw_packs = pack_box.split('\n\n')
    return [build_items(raw_pack) for raw_pack in raw_packs]


def build_items(pack):
    units = [u.split(' ') for u in pack.split('\n')]
    return [Box(b[0], b[1], b[2]) for b in units]


Box1 = Box(30, 40, 80)
Box2 = Box(80, 50, 40)
Box3 = Box(50, 80, 60)

test1 = '40 10 25\n40 30 30\n15 20 10\n10 30 10\n30 15 10'
test2 = '10 15 30\n20 10 20\n\n10 10 10\n20 20 20\n30 10 10'

packs = build_packs(test1)


def swap_d(item): # Rotation
    if item.swap_num == 0:
        item.height, item.width, item.depth = item.width, item.depth, item.height
    elif item.swap_num == 1:
        item.height, item.width, item.depth = item.depth, item.height, item.width
    elif item.swap_num == 2:
        item.height, item.width, item.depth = item.depth, item.height, item.width

def put_item(item, model_box):



flagBox = 1
for item in packs:
    if flagBox == 1:'''

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