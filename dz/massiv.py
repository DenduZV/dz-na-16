class Array:
    def __init__(self, capacity):
        if capacity < 0:
            raise ValueError('Размер не может быть отрицательным')
        self.data = [None] * capacity
        self.size = 0

    def append(self, value):
        if self.size == len(self.data):
            raise OverflowError('Массив заполнен')
        self.data[self.size] = value
        self.size += 1

    def check_index(self, index):
        if index < 0 or index >= self.size:
            raise IndexError('Неверный индекс')

    def get(self, index):
        self.check_index(index)
        return self.data[index]

    def set(self, index, value):
        self.check_index(index)
        self.data[index] = value

    def delete(self, index):
        self.check_index(index)
        value = self.data[index]
        for i in range(index, self.size - 1):
            self.data[i] = self.data[i + 1]
        self.size -= 1
        self.data[self.size] = None
        return value

    def find(self, value):
        for i in range(self.size):
            if self.data[i] == value:
                return i
        return -1

    def to_list(self):
        return self.data[:self.size]

    def __len__(self):
        return self.size
