class MyHashMap:
    def __init__(self):
        self.data = [-1] * 1000001

    def put(self, key, val):
        self.data[key] = val

    def get(self, key):
        return self.data[key]

    def remove(self, key):
        self.data[key] = -1
