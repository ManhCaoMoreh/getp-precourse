class MinHeap:
    def __init__(self):
        self.heap = []

    def rotate(self, node):
        left_node = 2 * node
        right_node = 2 * node + 1

        min_node = node
        if left_node < len(self.heap) and self.heap[min_node - 1] > self.heap[left_node - 1]:
            min_node = left_node
        if right_node < len(self.heap) and self.heap[min_node - 1] > self.heap[right_node - 1]:
            min_node = right_node

        if min_node != node:
            self.heap[min_node - 1], self.heap[node - 1] = self.heap[node - 1], self.heap[min_node - 1]
            self.rotate(min_node)

    def push(self, value):
        self.heap.append(value)
        node = len(self.heap)
        while node > 1:
            parent_node = node // 2
            if self.heap[parent_node-1] > self.heap[node-1]:
                self.heap[parent_node-1], self.heap[node-1] = self.heap[node-1], self.heap[parent_node-1]
                node = parent_node
            else:
                break
        pass

    def pop(self):
        if len(self.heap) == 0:
            raise IndexError("MinHeap is empty")

        top_value = self.heap[0]

        self.heap[0] = self.heap[len(self.heap) - 1]
        self.heap.pop()

        if len(self.heap) > 0:
            self.rotate(1)

        return top_value

    def heapify(self):
        for node in range(len(self.heap)//2, -1, -1):
            self.rotate(node)

    def is_empty(self):
        return len(self.heap) == 0


if __name__ == "__main__":
    min_heap = MinHeap()

    with open('input_heap.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            value = int(line.strip())
            min_heap.push(value)

    print("Min heap : ", min_heap.heap)
