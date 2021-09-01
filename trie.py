


## Creating a Trie - > Needs something to hold all of the Nodes, and needs each node to be it's own thing
## 

class TrieNode:
    # end of a word? what if it's the end of multiple words? that makes no sense, then they are the same word yes?
    def __init__(self, char, end_of_word=False):
        self.char = char
        self.end_of_word = end_of_word
        # can have up to 26 children, one for each letter of the alphabet
        self.children = []


class Trie:

    def __init__(self):
        super().__init__()
        self.root_node = TrieNode("")
    
    def insert(self, word):
        # starting from root node, gotta add one character at a time
        current_node = self.root_node

        for char in word:
            # if there is a child of the current node with this letter, then we update current node.
            # if not a child yet, create a new node with the char, add to children, and update current node
            found_match = False
            for child_node in current_node.children:
                if child_node.char == char:
                    current_node = child_node
                    found_match = True
                    break

            if not found_match:
                new_node = TrieNode(char)
                current_node.children.append(new_node)
                current_node = new_node

        current_node.end_of_word = True

    def search(self, word):
        letters_searched = []

        current_node = self.root_node
        for char in word:
            found_match = False
            for child_node in current_node.children:
                if child_node.char == char:
                    letters_searched.append(char)
                    current_node = child_node
                    found_match = True
                    break

            if not found_match:
                # break out of loop, because this letter had nothing attached
                print("didn't find anything, should fail")
                break

        word_found = (word == ''.join(letters_searched))
        return word_found, letters_searched

def test_trie():
    word_list = ['taco', 'dog', 'tank']

    trie = Trie()
    for word in word_list:
        trie.insert(word)

    search_list = ['babe', 'taco', 'superpowers', 'tankatsu', '']
    for word in search_list:
        found, letters_searched = trie.search(word)
        print(f'SEARCH:{word} -- {found}:{letters_searched}')


if __name__ == '__main__':
    test_trie()