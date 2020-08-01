class RingBuffer:
    def __init__(self, capacity):
        self.elements = []
        self.capacity = capacity

    def append(self, item):
        if len(self.elements) < self.capacity:
            self.elements.append(item)
        else:
            self.elements[0] = item

    def get(self):
        return self.elements



buffer = RingBuffer(5)
buffer.append('a')
buffer.append('b')
buffer.append('c')
buffer.append('d')
buffer.append('e')
buffer.append('e')
print(buffer.get())