# Uses python3


class TrieNode:
	def __init__(self, letter=''):
		self.letter = letter
		self.children = {}
		self.isWord = False


class Trie:
	def __init__(self):
		self.root = TrieNode()

	def add_word(self, word):
		curr = self.root
		for char in word:
			if char not in curr.children:
				curr.children[char] = TrieNode(char)
			curr = curr.children[char]
		curr.isWord = True


def build_trie(patterns):
	tree = Trie()
	for p in patterns:
		tree.add_word(p)
	return tree


def trie_matching(text, tree):

	def search(tree, word):
		curr = tree.root
		for char in word:
			if char not in curr.children:
				return False
			curr = curr.children[char]
			if curr.isWord:
				return True
	out = []
	for i in range(len(text)):
		if search(tree, text[i:]):
			out.append(i)
	return out


if __name__ == '__main__':
	text = input()
	n = int(input())
	patterns = []
	for _ in range(n):
		patterns.append(input())
	tree = build_trie(patterns)
	res = trie_matching(text, tree)
	print(*res)