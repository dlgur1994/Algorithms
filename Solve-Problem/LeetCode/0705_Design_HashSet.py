class MyHashSet:
    def __init__(self):
        self.my_hash = {}

    def add(self, key: int) -> None:
        self.my_hash[key] = "dummy"

    def remove(self, key: int) -> None:
        if key in self.my_hash:
            del self.my_hash[key]

    def contains(self, key: int) -> bool:
        if key in self.my_hash:
            return True
        else:
            return False

obj = MyHashSet()
obj.add(1)
obj.add(2)
obj.remove(1)
param_1 = obj.contains(1)
print(param_1)
