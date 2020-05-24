In this problem, I have to implement a Trie, which is a tree like structure that stores a dynamic set of strings.
Here first I have made a class for TrieNode which has insert & suffixes methods.
Trie class is made with the insert word & find methods.

Talking about the complexity of this data structure:

Time Complexity:
Insert loops over all character in the given word - O(n).
Find loops over all characters in the given prefix - O(n).
Suffixes loops over all TrieNodes in children, and calls itself m times -O(mn)
Space Complexity:
Worst case would be when words with no common characters between them, therefore having
a node for each letter -O(n)
where m is maximum number of elements one level can have & n is the number of levels.
