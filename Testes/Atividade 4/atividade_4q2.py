class CustomList:
    def __init__(self, items):
        self.items = items

    def get(self, index):
        if index >= len(self.items) or index < 0:
            print("O indice que você está lidando não está na lista!")
            return ""
        return self.items[index]
    
custom_list =  CustomList([1, 3, 4, 5, 6, 7])
print(custom_list.get(0))
print(custom_list.get(8))