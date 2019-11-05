"""
Simple graph implementation
"""

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)




class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    
    def __init__(self):
        self.vertices = {}
    
    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()
    
    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
            self.vertices[v2].add(v1)
        else:
            raise IndexError("That vertex does not exist!")
    
   

    # BFT
    def bft(self, starting_vertex_id):
        # create an empty queue and enqueue the starting vertex ID
        q = Queue()
        q.enqueue(starting_vertex_id)
        # create a set to store the visited vertices
        visited = set()
        # while the queue is not empty
        while q.size() > 0:
            # Dequeue the first vertex
            v = q.dequeue()
            # if that vertex has not been visited
            if v not in visited:
                # mark it as visited (printing for a representation)
                print(v)
                visited.add(v)
                # then add all of it's neighbors to the back of the queue
                for next_vertex in self.vertices[v]:
                    q.enqueue(next_vertex)

    # DFT
    def dft(self, starting_vertex_id):
        # create an empty stack and push the starting vertex ID
        s = Stack()
        s.push(starting_vertex_id)
        # create a set to store the visited vertices
        visited = set()
        # while the stack is not empty
        while s.size() > 0:
            # pop the first vertex
            v = s.pop()
            # if that vertex has not been visited
            if v not in visited:
                # mark it as visited (printing for a representation)
                print(v)
                visited.add(v)
                # then add all of it's neighbors to the top of the stack
                for next_vertex in self.vertices[v]:
                    s.push(next_vertex)

    def dft_r(self, start_vert, visited=None):
        pass

    def dfs(self, start_vert, target_value, visited=None):
        pass

    def bfs(self, starting_vertex_id, target_value):
        pass

    def dfs_r_path(self, start_vert, target_value, visited=None, path=None):
        pass

    def bfs_path(self, starting_vertex_id, target_value):
        pass

    def dfs_path(self, starting_vertex_id, target_value):
        pass
