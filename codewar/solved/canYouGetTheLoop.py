class Node(object):
    def __init__(self):
        self.next = None
        
# Too much time consuming, naive impl
#def loop_size(node):
#    found = []
#    while id(node) not in found:
#        found.append(id(node))
#        node = node.next
#    return len(found[found.index(id(node):])

def loop_size(node):
    found = False
    visitedNodes = 1
    while not found:
        try:
            found = node.visited
        except AttributeError:
            visitedNodes += 1
            node.visited = visitedNodes
        node = node.next
    return visitedNodes - found + 1

def create_chain(nbNode, loopSize):
    nodes = [Node() for _ in xrange(nbNode)]
    for node, next_node in zip(nodes, nodes[1:]):
        node.next = next_node
    nodes[nbNode-1].next = nodes[nbNode-loopSize]
    return nodes[0]

# Make a short chain with a loop of 3
chain = create_chain(4, 3)
print(loop_size(chain), 3, 'Loop size of 3 expected')


# Make a longer chain with a loop of 29
chain = create_chain(50, 29)
print(loop_size(chain), 29, 'Loop size of 29 expected')

# Make a very long chain with a loop of 1087
chain = create_chain(3904, 1087)
print(loop_size(chain), 1087, 'Loop size of 1087 expected')

# Make a very long chain with a loop of 1087
chain = create_chain(39040, 10857)
print(loop_size(chain), 10857, 'Loop size of 10857 expected')
