class Packer:
    def __init__(self):
        self.boxes = []
        self.items = []
        self.unfit_items = []

    def add_box(self, box):
        return self.boxes.append(box)

    def add_item(self, item):
        return self.items.append(item)

    def print_boxes(self):
        for b in self.boxes:
            print(':::::::::::')
            print(f'{b.name}')
            print('Itens colocados na caixa:')
            for item in b.items:
                print(
                    f'====> {item.height}x{item.width}x{item.depth}\n Pos: {item.position}\n Rot: {item.rotation_type}')
            print('Itens fora da caixa:')
            for item in b.unfitted_items:
                print(
                    f'==>Item {item.height}x{item.width}x{item.depth}\t Pos: {item.position}\t Rot: {item.rotation_type}')

    def pack_to_bin(self, box, item):
        fitted = False
        if not box.items:
            response = box.put_item(item, [0, 0, 0]) # posição inicial
            if not response:
                box.unfitted_items.append(item)
            return
        for axis in range(0, 3): # verifica possíveis pivos
            items_in_bin = box.items
            for ib in items_in_bin:
                pivot = [0, 0, 0]
                h, w, d = ib.get_dimension()
                if axis == 0:
                    pivot = [
                        ib.position[0] + h,
                        ib.position[1],
                        ib.position[2]
                    ]
                elif axis == 1:
                    pivot = [
                        ib.position[0],
                        ib.position[1] + w,
                        ib.position[2]
                    ]
                elif axis == 2:
                    pivot = [
                        ib.position[0],
                        ib.position[1],
                        ib.position[2] + d
                    ]
                if box.put_item(item, pivot):
                    fitted = True
                    break
            if fitted:
                break
        if not fitted:
            box.unfitted_items.append(item)

    def pack(self):
        self.items.sort(key=lambda item: item.volume, reverse=True) # ordenar do maior pro menor (premissa da heurística)
        for box in self.boxes:
            for item in self.items:
                self.pack_to_bin(box, item)
