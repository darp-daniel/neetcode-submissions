class DynamicArray:
    
    def __init__(self, capacity: int):
        if capacity == 0:
            return
        self.capacity = capacity
        self.Array = []

    def get(self, i: int) -> int:
        return self.Array[i]

    def set(self, i: int, n: int) -> None:
        self.Array[i] = n

    def pushback(self, n: int) -> None:
        if len(self.Array) == self.capacity:
            self.resize()
        self.Array.append(n)

    def popback(self) -> int:
        p = self.Array[-1]
        self.Array.pop()
        return p

    def resize(self) -> None:
        self.capacity = self.capacity * 2


    def getSize(self) -> int:
        return len(self.Array)
    
    def getCapacity(self) -> int:
        return self.capacity
