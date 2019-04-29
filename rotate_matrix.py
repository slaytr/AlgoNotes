class Matrix:
    def __init__(self, size):
        self.matrix_dim = size  # [height, width]
        self.matrix_size = self.matrix_dim - 1
        self.matrix = []
        self.matrix_construct()

    def __repr__(self):
        matrix_repr = ""
        for index, row in enumerate(self.matrix):
            matrix_repr = matrix_repr + str(row)
            if index != self.matrix_size:
                matrix_repr = matrix_repr + "\n"
        return matrix_repr

    def __len__(self):
        return len(self.matrix)

    def __contains__(self, item):
        return item in self.matrix

    def __iter__(self):
        return iter(self.matrix)

    def __reversed__(self):
        return reversed(self.matrix)

    def matrix_construct(self, vertical=True):
        """
        :bool vertical: If True, creates columns of the same number, otherwise rows
        """
        for i in range(self.matrix_dim):
            if vertical:
                row = []
                for j in range(self.matrix_dim):
                    row.append(j)
            else:
                row = [i] * self.matrix_dim
            self.matrix.append(row)

    def find_layers(self):
        return len(self.matrix)//2 +1 if len(self.matrix) % 2 == 1 else len(self.matrix)//2

    def rotate_outer(self):
        """
        Rotates the outer layer once
        """
        for index in range(self.matrix_size):
            temp = self.matrix[index][-1]
            self.matrix[index][-1] = self.matrix[0][index]
            self.matrix[0][index] = self.matrix[self.matrix_size-index][0]
            self.matrix[self.matrix_size - index][0] = self.matrix[self.matrix_size][self.matrix_size-index]
            self.matrix[self.matrix_size][self.matrix_size - index] = temp

    def rotate_layer(self, layer_number, iterations=1, show=False):
        """
        :int layer_number: range(1, N) 1 being the innermost layer, N being the outer layer
        :int iterations: Number of times to rotate the layer
        :bool show: Print the matrix if True
        :return: Layer No. and times rotated
        """
        max_layer = self.find_layers()

        if max_layer < layer_number or layer_number <= 0:
            raise ValueError
        elif max_layer == layer_number:
            self.rotate_outer()
        else:
            depth = max_layer - layer_number
            for _ in range(iterations):
                for index in range(depth, self.matrix_size-depth):
                    temp = self.matrix[index][-1-depth]
                    self.matrix[index][-1-depth] = self.matrix[depth][index]
                    self.matrix[depth][index] = self.matrix[self.matrix_size-index][depth]
                    self.matrix[self.matrix_size - index][depth] = \
                        self.matrix[self.matrix_size - depth][self.matrix_size - index]
                    self.matrix[self.matrix_size - depth][self.matrix_size - index] = temp
        if show:
            print(self)
            print("")
        return f"Layer Number: {layer_number} rotated {iterations} times \n"

def my_tests():
    obj = Matrix(8)
    print(obj.rotate_layer(1, 3))
    print(obj.rotate_layer(3, 1))
    print(obj.rotate_layer(2, 2, True))

    # TESTS

    # __repr__
    print("string representation test")
    print(obj)

    # __len__
    print("length test:", len(obj))

    # __iter__
    print("__iter__ test")
    for i in obj:
        print(i)

    # __reversed__
    print("reversed test")
    for i in reversed(obj):
        print(i)

    # __contains__
    print("__contains__ aka \'in\' test")
    print([0, 1, 2, 3, 4, 5, 6, 7] in obj)

if __name__ == "__main__":
    my_tests()

