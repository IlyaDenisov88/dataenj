## Стек - добавление в конец, извлевение из конца LIFO (last in, first out)

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

# Пример использования:
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print("Стек после добавления элементов:", stack.items)
print("Верхний элемент стека:", stack.peek())
print("Размер стека:", stack.size())
print("Извлечение элемента из стека:", stack.pop())
print("Стек после извлечения элемента:", stack.items)


## Очередь (Queue)

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)

    def front(self):
        if not self.is_empty():
            return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

# Пример использования:
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print("Очередь после добавления элементов:", queue.items)
print("Первый элемент очереди:", queue.front())
print("Размер очереди:", queue.size())
print("Извлечение элемента из очереди:", queue.dequeue())
print("Очередь после извлечения элемента:", queue.items)


## Односвязанный список 

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")

# Пример использования:
llist = LinkedList()
llist.append(1)
llist.append(2)
llist.append(3)
llist.print_list()  # Вывод: 1 -> 2 -> 3 -> None


## Двусвязанный список (ссылки на следующую и предыдущую ноды)

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        new_node.prev = last_node
        self.tail = new_node

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" <-> ")
            current_node = current_node.next
        print("None")

    def print_list_reverse(self):
        current_node = self.tail
        while current_node:
            print(current_node.data, end=" <-> ")
            current_node = current_node.prev
        print("None")

# Пример использования:
dllist = DoublyLinkedList()
dllist.append(1)
dllist.append(2)
dllist.append(3)
dllist.print_list()  # Вывод: 1 <-> 2 <-> 3 <-> None
dllist.print_list_reverse() # Вывод: 3 <-> 2 <-> 1 <-> None





## Дерево
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child):
        self.children.append(child)

# Пример использования:
root = TreeNode("A")
child1 = TreeNode("B")
child2 = TreeNode("C")
root.add_child(child1)
root.add_child(child2)



## Бинарное дерево 
class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = TreeNode(key)
        else:
            self._insert(self.root, key)

    def _insert(self, root, key):
        if key < root.val:
            if root.left is None:
                root.left = TreeNode(key)
            else:
                self._insert(root.left, key)
        else:
            if root.right is None:
                root.right = TreeNode(key)
            else:
                self._insert(root.right, key)

# Пример использования
bst = BinarySearchTree()
bst.insert(10)
bst.insert(5)
bst.insert(15)
bst.insert(3)
bst.insert(7)



def search(root, key):
    if root is None or root.val == key:
        return root
    if key < root.val:
        return search(root.left, key)
    return search(root.right, key)

# Пример использования
found_val = 7
found_node = search(bst.root, found_val)
if found_node:
    print("Элемент найден:", found_node.val)
else:
    print("Элемент", found_val, "не найден")
    

found_val = 11
found_node = search(bst.root, found_val)
if found_node:
    print("Элемент найден:", found_node.val)
else:
    print("Элемент", found_val, "не найден")



## Алгоритмы обхода
## В глубину
	## Для деревьев:
		## Рекурсивный подход:

		class TreeNode:
		    def __init__(self, data):
			self.data = data
			self.children = []

		    def add_child(self, child):
			self.children.append(child)

		    def dfs_traversal(self):
			print(self.data)  # Посещаем текущий узел
			for child in self.children:
			    child.dfs_traversal()  # Рекурсивный вызов для каждого дочернего узла

		# Пример использования:
		root = TreeNode("A")
		child1 = TreeNode("B")
		child2 = TreeNode("C")
		root.add_child(child1)
		root.add_child(child2)
		child1.add_child(TreeNode("D"))
		child1.add_child(TreeNode("E"))
		root.dfs_traversal()  # Вывод: A B D E C
		
		## Итеративный подход с использованием стека:
		class TreeNode:
		    def __init__(self, data):
			self.data = data
			self.children = []

		    def add_child(self, child):
			self.children.append(child)

		    def dfs_traversal(self):
			stack = [self]  # Используем стек, инициализируем корнем
			while stack:
			    node = stack.pop()  # Извлекаем текущий узел из стека
			    print(node.data)  # Посещаем текущий узел
			    stack.extend(reversed(node.children))  # Добавляем дочерние узлы в стек

		# Пример использования:
		root = TreeNode("A")
		child1 = TreeNode("B")
		child2 = TreeNode("C")
		root.add_child(child1)
		root.add_child(child2)
		child1.add_child(TreeNode("D"))
		child1.add_child(TreeNode("E"))
		root.dfs_traversal()  # Вывод: A B D E C
		
		
	## Для графов:
		## Рекурсивный подход:
		class Graph:
		    def __init__(self):
			self.graph = {}

		    def add_edge(self, node, neighbor):
			if node not in self.graph:
			    self.graph[node] = []
			self.graph[node].append(neighbor)

		    def dfs_traversal(self, node, visited=None):
			if visited is None:
			    visited = set()
			visited.add(node)
			print(node)  # Посещаем текущий узел
			for neighbor in self.graph.get(node, []):
			    if neighbor not in visited:
				self.dfs_traversal(neighbor, visited)  # Рекурсивный вызов для каждого соседнего узла

		# Пример использования:
		graph = Graph()
		graph.add_edge("A", "B")
		graph.add_edge("A", "C")
		graph.add_edge("B", "D")
		graph.add_edge("B", "E")
		graph.add_edge("C", "F")
		graph.dfs_traversal("A")  # Вывод: A B D E C F
		
		
		## Итеративный подход с использованием стека:
		class Graph:
		    def __init__(self):
			self.graph = {}

		    def add_edge(self, node, neighbor):
			if node not in self.graph:
			    self.graph[node] = []
			self.graph[node].append(neighbor)

		    def dfs_traversal(self, start_node):
			visited = set()
			stack = [start_node]  # Используем стек, инициализируем начальной вершиной
			while stack:
			    node = stack.pop()  # Извлекаем текущую вершину из стека
			    if node not in visited:
				print(node)  # Посещаем текущую вершину
				visited.add(node)
				for neighbor in reversed(self.graph.get(node, [])):
				    if neighbor not in visited:
				        stack.append(neighbor)  # Добавляем соседей в стек

		# Пример использования:
		graph = Graph()
		graph.add_edge("A", "B")
		graph.add_edge("A", "C")
		graph.add_edge("B", "D")
		graph.add_edge("B", "E")
		graph.add_edge("C", "F")
		graph.dfs_traversal("A")  # Вывод: A C F B E D

## Реализация обхода в ширину:
	## Для деревьев:
		## Реализация с использованием очереди:
		
		class TreeNode:
		    def __init__(self, data):
			self.data = data
			self.children = []

		    def add_child(self, child):
			self.children.append(child)

		    def bfs_traversal(self):
			queue = [self]  # Инициализируем очередь с корнем
			while queue:
			    node = queue.pop(0)  # Извлекаем текущий узел из начала очереди
			    print(node.data)  # Посещаем текущий узел
			    for child in node.children:
				queue.append(child)  # Добавляем дочерние узлы в очередь

		# Пример использования:
		root = TreeNode("A")
		child1 = TreeNode("B")
		child2 = TreeNode("C")
		root.add_child(child1)
		root.add_child(child2)
		child1.add_child(TreeNode("D"))
		child1.add_child(TreeNode("E"))
		root.bfs_traversal()  # Вывод: A B C D E
		
	## Для графов:
		## Реализация с использованием очереди:
		
		class Graph:
		    def __init__(self):
			self.graph = {}

		    def add_edge(self, node, neighbor):
			if node not in self.graph:
			    self.graph[node] = []
			self.graph[node].append(neighbor)

		    def bfs_traversal(self, start_node):
			visited = set()
			queue = [start_node]  # Инициализируем очередь с начальной вершиной
			visited.add(start_node)
			while queue:
			    node = queue.pop(0)  # Извлекаем текущую вершину из начала очереди
			    print(node)  # Посещаем текущую вершину
			    for neighbor in self.graph.get(node, []):
				if neighbor not in visited:
				    visited.add(neighbor)
				    queue.append(neighbor)  # Добавляем соседей в очередь

		# Пример использования:
		graph = Graph()
		graph.add_edge("A", "B")
		graph.add_edge("A", "C")
		graph.add_edge("B", "D")
		graph.add_edge("B", "E")
		graph.add_edge("C", "F")
		graph.bfs_traversal("A")  # Вывод: A B C D E F



