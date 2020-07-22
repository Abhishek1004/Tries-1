class TrieNode:
    def __init__(self):
        self.end = False
        self.child_nodes = [None for _ in range(26)]
        
class Solution:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        curr = self.root
        for letter in word:
            if not curr.child_nodes[ord(letter)-ord('a')]:
                curr.child_nodes[ord(letter)-ord('a')] = TrieNode()
            curr = curr.child_nodes[ord(letter)-ord('a')]
        curr.end = True
        
    def replaceWords(self, dict: List[str], sentence: str) -> str:
        for word in dict:
            self.insert(word)
        worded = sentence.split(' ')
        result = []
        for word in worded:
            curr = self.root
            replacement = []
            for letter in word:
                if curr.child_nodes[ord(letter)-ord('a')]:
                    replacement.append(letter)
                    if curr.child_nodes[ord(letter)-ord('a')].end == True:
                        break
                    else:
                        curr = curr.child_nodes[ord(letter)-ord('a')]
                else:
                    replacement = word
                    break
            result.append(''.join(replacement))
        return " ".join(result)

#time complexity - O(m*n), m = avg. length of words, n = total words

#space complexity - O(m). m = avg. length of words

#all test cases passed