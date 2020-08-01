class RingBuffer:
    def __init__(self, capacity):
        self.elements = []
        self.capacity = capacity
        self.index = 0

    def append(self, item):
        if len(self.elements) == self.capacity:
            self.elements[self.index] = item
            self.index = (self.index + 1) % self.capacity

        else:
            self.elements.append(item)

            if len(self.elements) == self.capacity:
                self.index = 0

    def get(self):
        return self.elements



buffer = RingBuffer(3)
buffer.append('a')
buffer.append('b')
buffer.append('c')
buffer.append('d')
buffer.append('e')
buffer.append('f')
buffer.append('g')
buffer.append('h')
print(buffer.get())