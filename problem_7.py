# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, root_handler=None):
    # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode(root_handler)
    def insert(self, path, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        path_parts = self.split_path(path)
        node = self.root
        for part in path_parts:
            if part != '':
                node = node.children[part]
        node.handler = handler
    def find(self, path):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        #A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
        path_parts = self.split_path(path)
        node = self.root
        for part in path_parts:
            if part != '':
                node = node.children[part]
        return node.handler
    def split_path(self, path):
        return path.split('/')
from collections import defaultdict
class RouteTrieNode:
    def __init__(self, handler=None):
     # Initialize the node with children as before, plus a handler
        self.children = defaultdict(RouteTrieNode)
        self.handler = handler
class Router:
    def __init__(self, root_handler): 
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.route_trie = RouteTrie(root_handler)

    def add_handler(self, path, handler): 
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        if path == self.root:
        self.route_trie.insert(path, handler)

    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        return self.route_trie.find(path)
router = Router("root handler")
router.add_handler("/home/about","about handler") 
router.add_handler("/home", "home handler")
router.add_handler("/home/about", "about handler")
router.add_handler("/home/about/me/edit", "edit handler")
print(router.lookup("/")) 
print(router.lookup("/home"))
print(router.lookup("/home/about")) 
print(router.lookup("/home/about/"))
print(router.lookup("/home/about/me"))
router.lookup("/home/about")