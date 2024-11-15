class TreeStore:
    def __init__(self, items):
        self.items_by_id = {item['id']: item for item in items}
        self.children_by_parent_id = {}

        for item in items:
            parent_id = item['parent']
            if parent_id not in self.children_by_parent_id:
                self.children_by_parent_id[parent_id] = []
            self.children_by_parent_id[parent_id].append(item)

    def getAll(self):
        return list(self.items_by_id.values())

    def getItem(self, id):
        return self.items_by_id.get(id)

    def getChildren(self, id):
        return self.children_by_parent_id.get(id, [])

    def getAllParents(self, id):
        parents = []
        current_id = id
        while current_id in self.items_by_id:
            current_item = self.items_by_id[current_id]
            parents.append(current_item)
            current_id = current_item['parent']
        return parents[1:]

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

