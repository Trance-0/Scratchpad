class TrieNode:
    def __init__(self,end=10**10):
        self.children = {}
        self.cost = end
        self.end = end

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word, cost):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.cost = min(cost, node.cost)
    
    def search(self, s, start):
        node = self.root
        matches = []
        for i in range(start, len(s)):
            if s[i] in node.children:
                node = node.children[s[i]]
                if node.cost < self.end:
                    matches.append((i + 1, node.cost))
            else:
                break
        return matches