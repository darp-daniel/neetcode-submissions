class LinkedList:
    
    def __init__(self):
        self.lin_list = []
    
    def get(self, index: int) -> int:
        if index > (len(self.lin_list) - 1):
            return -1
        return self.lin_list[index]

    def insertHead(self, val: int) -> None:
        arr = [val]
        for v in self.lin_list:
            arr.append(v)
        self.lin_list = arr

    def insertTail(self, val: int) -> None:
        self.lin_list.append(val)

    def remove(self, index: int) -> bool:
        if index > (len(self.lin_list) - 1):
            return False
        self.lin_list.pop(index)
        return True
        

    def getValues(self) -> List[int]:
        return self.lin_list
        
