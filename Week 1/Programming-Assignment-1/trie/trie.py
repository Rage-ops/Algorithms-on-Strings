# Uses python3

# Return the trie built from patterns
# in the form of a dictionary of dictionaries,
# e.g. {0:{'A':1,'T':2},1:{'C':3}}
# where the key of the external dictionary is
# the node ID (integer), and the internal dictionary
# contains all the trie edges outgoing from the corresponding
# node, and the keys are the letters on those edges, and the
# values are the node IDs to which these edges lead.

class TrieNode:
    def __init__(self, text='', index=0):
        self.text = text
        self.children = {}
        self.index = index


class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.c = 0

    def add_word(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                self.c += 1
                curr.children[char] = TrieNode(char, self.c)
            curr = curr.children[char]


def explore(node, parent):
    if node.text:
        print("{}->{}:{}".format(parent, node.index, node.text))
    for value in node.children.values():
        explore(value, node.index)


def build_trie(patterns):
    # tree = dict()
    tree = Trie()
    for p in patterns:
        tree.add_word(p)
    return tree


if __name__ == '__main__':
    n = int(input())
    patterns = [input() for _ in range(n)]
    tree = build_trie(patterns)
    explore(tree.root, 0)
    # print(tree)
    # for node in tree:
    #     for c in tree[node]:
    #         print("{}->{}:{}".format(node, tree[node][c], c))
