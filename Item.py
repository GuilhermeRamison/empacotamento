class Item:
    def __init__(self, height, width, depth):
        self.height = int(height)
        self.width = int(width)
        self.depth = int(depth)
        self.volume = self.depth * self.height * self.width
        self.rotation_type = 0  # rotação inicial: (x, y, z)
        self.position = (0, 0, 0)  # posição inicial: (0, 0, 0)

    def get_dimension(self):  # 6 tipos de rotação -- (x-axis, y-axis, z-axis)
        if self.rotation_type == 0:
            dimension = [self.height, self.width, self.depth]
        elif self.rotation_type == 1:
            dimension = [self.width, self.height, self.depth]
        elif self.rotation_type == 2:
            dimension = [self.height, self.depth, self.width]
        elif self.rotation_type == 3:
            dimension = [self.depth, self.height, self.width]
        elif self.rotation_type == 4:
            dimension = [self.depth, self.width, self.height]
        elif self.rotation_type == 5:
            dimension = [self.width, self.depth, self.height]
        else:
            dimension = []

        return dimension
