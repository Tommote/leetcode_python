
class MaxHeap():
    """
    最大堆
    """
    def __init__(self):
        self._count = 0
        self._data = [0]

    def shift_up(self, index):
        while index > 1 and self._data[index // 2] < self._data[index]:
            self._data[index // 2], self._data[index] = self._data[index], self._data[index // 2]
            index //= 2

    def insert(self, value):
        self._data.append(value)
        self._count += 1
        self.shift_up(self._count)

    def print(self):
        print(self._data[1:])

    def extract_max(self):
        cur_max = self._data[1]
        self._data[1], self._data[self._count] = self._data[self._count], self._data[1]
        self._count -= 1
        self.shift_down(1)
        return cur_max

    def shift_down(self, index):
        while index * 2 <= self._count:
            m = index * 2
            if m + 1 <= self._count and self._data[m + 1] > self._data[m]:
                m = index * 2 + 1 

            if self._data[index] > self._data[m]:
                break

            self._data[index], self._data[m] = self._data[m], self._data[index]
            index = m