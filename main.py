# Реализация структур данных с использованием списков

# Реализация стека
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        """Добавить элемент в стек."""
        self.stack.append(item)

    def pop(self):
        """Удалить и вернуть верхний элемент стека."""
        if not self.is_empty():
            return self.stack.pop()
        return None

    def peek(self):
        """Посмотреть верхний элемент стека, не удаляя его."""
        if not self.is_empty():
            return self.stack[-1]
        return None

    def is_empty(self):
        """Проверить, пуст ли стек."""
        return len(self.stack) == 0

# Реализация очереди
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        """Добавить элемент в конец очереди."""
        self.queue.append(item)

    def dequeue(self):
        """Удалить и вернуть первый элемент очереди."""
        if not self.is_empty():
            return self.queue.pop(0)
        return None

    def peek(self):
        """Посмотреть первый элемент очереди, не удаляя его."""
        if not self.is_empty():
            return self.queue[0]
        return None

    def is_empty(self):
        """Проверить, пуста ли очередь."""
        return len(self.queue) == 0

# Реализация дерева
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child_node):
        """Добавить дочерний узел."""
        self.children.append(child_node)

    def __str__(self, level=0):
        """Печать дерева."""
        ret = "  " * level + str(self.value) + "\n"
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret

# Реализация графа
class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        """Добавить вершину в граф."""
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, vertex1, vertex2):
        """Добавить ребро между двумя вершинами."""
        if vertex1 in self.graph and vertex2 in self.graph:
            self.graph[vertex1].append(vertex2)
            self.graph[vertex2].append(vertex1)

    def get_neighbors(self, vertex):
        """Получить список соседей вершины."""
        return self.graph.get(vertex, [])

    def __str__(self):
        """Печать графа."""
        result = ""
        for vertex, edges in self.graph.items():
            result += f"{vertex} -> {', '.join(edges)}\n"
        return result

# Пример использования
if __name__ == "__main__":
    # Пример использования стека
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print("Стек после добавления элементов:", stack.stack)
    print("Верхний элемент стека:", stack.peek())
    print("Извлечённый элемент:", stack.pop())
    print("Стек после извлечения элемента:", stack.stack)

    # Пример использования очереди
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print("Очередь после добавления элементов:", queue.queue)
    print("Первый элемент очереди:", queue.peek())
    print("Извлечённый элемент:", queue.dequeue())
    print("Очередь после извлечения элемента:", queue.queue)

    # Пример использования дерева
    root = TreeNode("Корень")
    child1 = TreeNode("Ребёнок 1")
    child2 = TreeNode("Ребёнок 2")
    child3 = TreeNode("Ребёнок 3")
    root.add_child(child1)
    root.add_child(child2)
    root.add_child(child3)

    grandchild1 = TreeNode("Внук 1")
    grandchild2 = TreeNode("Внук 2")
    grandchild3 = TreeNode("Внук 3")
    child1.add_child(grandchild1)
    child2.add_child(grandchild2)
    child3.add_child(grandchild3)

    great_grandchild1 = TreeNode("Правнук 1")
    great_grandchild2 = TreeNode("Правнук 2")
    grandchild1.add_child(great_grandchild1)
    grandchild2.add_child(great_grandchild2)

    print("Структура дерева:")
    print(root)

    # Пример использования графа
    graph = Graph()
    graph.add_vertex("A")
    graph.add_vertex("B")
    graph.add_vertex("C")
    graph.add_vertex("D")
    graph.add_vertex("E")

    graph.add_edge("A", "B")
    graph.add_edge("A", "C")
    graph.add_edge("B", "D")
    graph.add_edge("C", "E")
    graph.add_edge("D", "E")

    print("Структура графа:")
    print(graph)