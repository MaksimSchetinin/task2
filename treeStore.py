
class TreeStore:
    def __init__(self, items):
        self.items = items

    def getAll(self):
        return self.items

    def getItem(self, id):
        return next((item for item in self.items if item["id"] == id), [])

    def getChildren(self, id):
        return [item for item in self.items if item['parent'] == id]

    def getAllParents(self, id):
        res = []
        item = self.getItem(id)
        while item:
            a = item['parent']
            item = self.getItem(a)
            if not item:
                break
            res.append(item)
        return res





items = [
    {"id": 1, "parent": "root"},
    {"id": 2, "parent": 1, "type": "test"},
    {"id": 3, "parent": 1, "type": "test"},
    {"id": 4, "parent": 2, "type": "test"},
    {"id": 5, "parent": 2, "type": "test"},
    {"id": 6, "parent": 2, "type": "test"},
    {"id": 7, "parent": 4, "type": None},
    {"id": 8, "parent": 4, "type": None}
]

def main():
    ts = TreeStore(items)
    print(ts.getAll())
    print(ts.getItem(7))
    print(ts.getItem(70))
    print(ts.getChildren(4))
    print(ts.getChildren(5))
    print(ts.getAllParents(7))
    print(ts.getAllParents(1))
    print(ts.getAllParents(70))

if __name__ == "__main__":
	main()
