"""
A prefix tree (also known as a trie) is a tree data structure used to efficiently store and retrieve keys in a set of strings. Some applications of this data structure include auto-complete and spell checker systems.

Implement the PrefixTree class:

PrefixTree() Initializes the prefix tree object.
void insert(String word) Inserts the string word into the prefix tree.
boolean search(String word) Returns true if the string word is in the prefix tree (i.e., was inserted before), and false otherwise.
boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.
Example 1:

Input: 
["Trie", "insert", "dog", "search", "dog", "search", "do", "startsWith", "do", "insert", "do", "search", "do"]

Output:
[null, null, true, false, true, null, true]

Explanation:
PrefixTree prefixTree = new PrefixTree();
prefixTree.insert("dog");
prefixTree.search("dog");    // return true
prefixTree.search("do");     // return false
prefixTree.startsWith("do"); // return true
prefixTree.insert("do");
prefixTree.search("do");     // return true
Constraints:

1 <= word.length, prefix.length <= 1000
word and prefix are made up of lowercase English letters.
"""




"""
Not optimum
"""
class PrefixTree:

    def __init__(self, char="", end=False):
        self.char = "char"
        self.children = {}
        self.end = end

    def insert(self, word: str) -> None:
        if not word:
            self.end = True
            return
        next_word = word[1:] if len(word)>1 else ""
        if word[0] in self.children:
            childTree = self.children[word[0]]
        else:
            childTree = PrefixTree(char=word[0])
            self.children[word[0]] = childTree
        childTree.insert(next_word)

    def search(self, word: str) -> bool:
        if not word:
            return self.end
        next_word = word[1:] if len(word)>1 else ""
        if word[0] in self.children:
            return self.children[word[0]].search(next_word)
        return False

    def startsWith(self, prefix: str) -> bool:
        if not prefix:
            return True
        next_word = prefix[1:] if len(prefix)>1 else ""
        if prefix[0] in self.children:
            return self.children[prefix[0]].startsWith(next_word)
        return False
        