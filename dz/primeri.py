from my_array import Array
from linked_list import LinkedList
from my_deque import Deque
from avl_tree import AVLTree
from sorting import bubble_sort, quick_sort


def main():
    arr = Array(5)
    arr.append(10)
    arr.append(20)
    arr.set(0, 15)
    print('Массив:', arr.to_list())

    items = LinkedList()
    items.append(2)
    items.prepend(1)
    items.append(3)
    items.delete(2)
    print('Список:', items.to_list())

    queue = Deque()
    queue.append(2)
    queue.append_left(1)
    queue.append(3)
    print('Дек:', queue.to_list())
    print('Удалили справа:', queue.pop())

    tree = AVLTree()
    for value in [30, 20, 10, 25, 40, 50]:
        tree.insert(value)
    print('АВЛ-дерево по возрастанию:', tree.to_list())
    tree.delete(30)
    print('После удаления 30:', tree.to_list())

    numbers = [1, 4, 8, 6, 7, 42, 2, 2, 8, 100, 3, 5]
    print('Пузырёк:', bubble_sort(numbers.copy()))
    print('Быстрая:', quick_sort(numbers.copy()))


if __name__ == '__main__':
    main()
