class Trie_node:
    def __init__(self):
        self.childnodes = [None for _ in range(26)]
        self.end = None

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Trie_node()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        curr = self.root
        for letter in word:
            if curr.childnodes[ord(letter)-ord('a')] == None:
                curr.childnodes[ord(letter)-ord('a')] = Trie_node()
            curr = curr.childnodes[ord(letter)-ord('a')]
        curr.end = True
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        curr = self.root
        for letter in word:
            if curr.childnodes[ord(letter)-ord('a')] == None:
                return False
            curr = curr.childnodes[ord(letter)-ord('a')]
        return curr.end
        
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        curr = self.root
        for letter in prefix:
            if curr.childnodes[ord(letter)-ord('a')] == None:
                return False
            curr = curr.childnodes[ord(letter)-ord('a')]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)



#time complexity - O(n)

#space complexity - O(n)

#all test cases passed