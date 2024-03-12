class CustomList:
    def __init__(self, items):
        self.items = items

    def delete(self, index):
        if index not in self.items:
          print("O valor não está na lista!")
          return self.items
        else:
          self.items.remove(index)
          print(f"{index} removido!")
        return self.items
    
custom_list = CustomList(["green", "blue", "yellow", "red", "purple"])

custom_list.delete("black")
custom_list.delete("blue")