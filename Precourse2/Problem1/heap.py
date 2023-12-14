class MinHeap:
    def __init__(self):
        self.heap = []

    def push(self, value):
        self.heap.append(value)
        current_node = len(self.heap)
        while current_node > 1:
            parent_node = current_node // 2
            if self.heap[parent_node-1] > self.heap[current_node-1]:
                self.heap[parent_node-1], self.heap[current_node-1] = self.heap[current_node-1], self.heap[parent_node-1]
                current_node = parent_node
            else:
                break
        pass

    def pop(self):
        top_value = self.heap[0]
        self.heap[0] = self.heap[len(self.heap)-1]
        self.heap.pop()
        current_node = 1
        while True:
            left_child_node = current_node*2
            right_child_node = current_node*2+1

            left_node_value = self.heap[current_node-1]+1
            if left_child_node < len(self.heap):
                left_node_value = self.heap[left_child_node]

            right_node_value = self.heap[current_node-1]+1
            if right_child_node < len(self.heap):
                right_node_value = self.heap[right_child_node]

            if min(left_node_value, right_node_value) >= self.heap[current_node-1]:
                break

            if left_node_value <= right_node_value:
                self.heap[current_node], self.heap[left_child_node] = self.heap[left_child_node], self[current_node]
                current_node = left_child_node
            else:
                self.heap[current_node], self.heap[right_child_node] = self.heap[right_child_node], self[current_node]
                current_node = right_child_node

        return top_value

    def heapify(self):
        # TODO : FILL IN HERE
        pass

if __name__ == "__main__":
    min_heap = MinHeap()

    with open('input_heap.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            value = int(line.strip())
            min_heap.push(value)

    print("Min heap : ", min_heap.heap)
