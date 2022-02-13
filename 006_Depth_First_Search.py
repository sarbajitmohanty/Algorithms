class Node:
    def __init__(self, name):
        self.childen = []
        self.name = name

    def addChild(self, name):
        self.childen.append(Node(name))

    # O(v + e) time | O(v) space
    def depthFirstSearch(self, array):
        array.append(self.name)
        for child in self.childen:
            child.depthFirstSearch(array)
        return array