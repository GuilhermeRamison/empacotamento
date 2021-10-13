def rect_intersect(item1, item2, x, y): # verifica se ocorre colisão dos itens 2d
    d1 = item1.get_dimension()
    d2 = item2.get_dimension()

    cx1 = item1.position[x] + d1[x]/2
    cy1 = item1.position[y] + d1[y]/2
    cx2 = item2.position[x] + d2[x]/2
    cy2 = item2.position[y] + d2[y]/2

    ix = max(cx1, cx2) - min(cx1, cx2)
    iy = max(cy1, cy2) - min(cy1, cy2)

    return ix < (d1[x]+d2[x])/2 and iy < (d1[y]+d2[y])/2


def intersect(item1, item2):  # verifica se ocorre colisão dos itens 3d
    return (
        rect_intersect(item1, item2, 0, 1) and
        rect_intersect(item1, item2, 1, 2) and
        rect_intersect(item1, item2, 0, 2)
    )


class Box:
    def __init__(self, name, height, width, depth):
        self.name = name
        self.height = height
        self.width = width
        self.depth = depth
        self.pivot = [0, 0, 0]
        self.pivot_list = []
        self.items = []
        self.unfitted_items = []

    def put_item(self, item, pivot):
        fit = False
        valid_item_position = item.position
        item.position = pivot
        for i in range(6):
            item.rotation_type = i
            dimension = item.get_dimension()
            if (
                    self.height < pivot[0] + dimension[0] or
                    self.width < pivot[1] + dimension[1] or
                    self.depth < pivot[2] + dimension[2]
            ): # verifica se o item não passa do tamanho da caixa de acordo com a posição
                continue
            fit = True
            for current_item_in_bin in self.items:
                if intersect(current_item_in_bin, item):
                    fit = False
                    break
            if fit:
                self.items.append(item)
            if not fit:
                item.position = valid_item_position
            return fit
        if not fit:
            item.position = valid_item_position
        return fit
