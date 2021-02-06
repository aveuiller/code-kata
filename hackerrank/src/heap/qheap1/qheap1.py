class Heap:
    def __init__(self) -> None:
        self.nodes = []
        self.to_delete = []

    @property
    def size(self):
        return len(self.nodes) - 1

    def add(self, value) -> None:
        if value not in self.nodes:
            self.nodes.append(value)
            self._raise(self.size)

    def delete(self, value) -> None:
        if self.nodes[0] != value:
            self.to_delete.append(value)
        else:
            while self.nodes[0] in self.to_delete:
                i = self.nodes.index(value)
                self.nodes[i] = self.nodes[self.size]
                self.nodes = self.nodes[:-1]
                self._sink(i)

    def _raise(self, index) -> None:
        if index > 0:
            parent_index = index // 2
            if self.nodes[parent_index] > self.nodes[index]:
                self.switch(index, parent_index)
                self._raise(parent_index)

    def _sink(self, index):
        if 2 * index < self.size:
            smallest_index = self._smallest_index(index)
            if self.nodes[smallest_index] < self.nodes[index]:
                self.switch(index, smallest_index)
                self._sink(smallest_index)

    def _smallest_index(self, index):
        left_i = 2 * index
        right_i = left_i + 1
        if left_i == self.size or self.nodes[left_i] < self.nodes[right_i]:
            return left_i
        else:
            return right_i

    def switch(self, index, parent_index):
        self.nodes[parent_index], self.nodes[index] = self.nodes[index], \
                                                      self.nodes[parent_index]

    def to_str(self, _) -> None:
        print(self.nodes[0])

    def default_op(self, _) -> None:
        print("Error!")


operations = {
    '1': Heap.add,
    '2': Heap.delete,
    '3': Heap.to_str
}


def fetch_stdin():
    q_count = int(input())
    for _ in range(q_count):
        yield str(input()).split(" ")


# Expected:
# 4
# 9
TEST_COMMANDS_1 = [
    ["1", "4"],
    ["1", "9"],
    ["3"],
    ["2", "4"],
    ["3"]
]

# Expected:
# 255653921
# 274310529
# 20842598
# -51159108
# 20842598
TEST_COMMANDS_2 = [
    ["1", "286789035"],
    ["1", "255653921"],
    ["1", "274310529"],
    ["1", "494521015"],
    ["3"],
    ["2", "255653921"],
    ["2", "286789035"],
    ["3"],
    ["1", "236295092"],
    ["1", "254828111"],
    ["2", "254828111"],
    ["1", "465995753"],
    ["1", "85886315"],
    ["1", "7959587"],
    ["1", "20842598"],
    ["2", "7959587"],
    ["3"],
    ["1", "-51159108"],
    ["3"],
    ["2", "-51159108"],
    ["3"],
    ["1", "789534713"],
]


def main():
    heap = Heap()
    for command in TEST_COMMANDS_2:
        operations.get(command[0], Heap.default_op)(heap, command[-1])


if __name__ == '__main__':
    main()
