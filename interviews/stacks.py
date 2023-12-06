"""
Implement a stack. (pop, push, peek, is_empty)
Implement a min stack. (pop, push, peek, is_empty, min)
"""
from abc import ABC, abstractmethod
from typing import Generic, Optional, TypeVar

T = TypeVar('T')

class Node(Generic[T]):
    def __init__(self, value: T) -> None:
        self.data = value
        self.next: Optional[Node] = None


class BaseStack(Generic[T], ABC):
    @abstractmethod
    def pop(self) -> T:
        ...

    @abstractmethod
    def push(self, item: T):
        ...

    @abstractmethod
    def peek(self) -> T:
        ...

    @abstractmethod
    def is_empty(self) -> bool:
        ...


class Stack(BaseStack[T]):
    def __init__(self) -> None:
        self.stack = []

    def pop(self) -> T:
        assert not self.is_empty(), "Stack is empty."

        return self.stack.pop(-1)

    def push(self, item: T):
        self.stack.append(item)

    def peek(self) -> T:
        assert not self.is_empty(), "Stack is empty."

        return self.stack[-1]

    def is_empty(self) -> bool:
        return len(self.stack) == 0


def test_stack() -> None:
    s = Stack()
    assert s.is_empty()
    s.push(1)
    s.push(2)
    s.push(3)
    assert s.peek() == 3
    assert not s.is_empty()
    assert s.pop() == 3
    assert s.peek() == 2


class MinStack(Stack[T]):
    def __init__(self) -> None:
        super().__init__()
        self.min_dict = {}
    
    def pop(self) -> T:
        del self.min_dict[len(self.stack) - 1]
        return super().pop()

    def push(self, item: T) -> None:
        if self.is_empty():
            new_min = item
        else:
            curr_min = self.min()
            new_min = item if item < curr_min else curr_min

        super().push(item)
        self.min_dict[len(self.stack) - 1] = new_min

    def min(self) -> T:
        assert not self.is_empty(), "Stack is empty."

        return self.min_dict[len(self.stack) - 1]


def test_min_stack() -> None:
    ms = MinStack()
    assert ms.is_empty()
    ms.push(10)
    assert ms.min() == 10
    ms.push(2)
    assert ms.min() == 2
    ms.push(3)
    ms.push(0)
    assert ms.peek() == ms.min()
    assert not ms.is_empty()
    assert ms.pop() == 0
    assert ms.peek() == 3
    assert ms.min() == 2


class MinStackV2(Stack[T]):
    def __init__(self) -> None:
        super().__init__()
        self.min_array = []
    
    def pop(self) -> T:
        self.min_array.pop(-1)
        return super().pop()

    def push(self, item: T) -> None:
        if self.is_empty():
            new_min = item
        else:
            curr_min = self.min()
            new_min = item if item < curr_min else curr_min

        super().push(item)
        self.min_array.append(new_min)

    def min(self) -> T:
        assert not self.is_empty(), "Stack is empty."

        return self.min_array[-1]


def test_min_stack_v2() -> None:
    msv2 = MinStackV2()
    assert msv2.is_empty()
    msv2.push(10)
    assert msv2.min() == 10
    msv2.push(2)
    assert msv2.min() == 2
    msv2.push(3)
    msv2.push(0)
    assert msv2.peek() == msv2.min()
    assert not msv2.is_empty()
    assert msv2.pop() == 0
    assert msv2.peek() == 3
    assert msv2.min() == 2


class LinkedStack(BaseStack[T]):
    def __init__(self) -> None:
        self.top: Optional[Node] = None

    def pop(self) -> T:
        assert self.top, "Stack is empty."
        curr = self.top.data
        self.top = self.top.next
        return curr

    def push(self, item: T):
        curr = Node(item)

        if self.is_empty():
            self.top = curr
        else:
            curr.next = self.top
            self.top = curr

    def peek(self) -> T:
        assert self.top, "Stack is empty."
        return self.top.data

    def is_empty(self) -> bool:
        return self.top is None


def test_linked_stack() -> None:
    ls = LinkedStack()
    assert ls.is_empty()
    ls.push(1)
    ls.push(2)
    ls.push(3)
    assert ls.peek() == 3
    assert not ls.is_empty()
    assert ls.pop() == 3
    assert ls.peek() == 2


class MinNode(Generic[T]):
    def __init__(self, value: T, min: T) -> None:
        self.data = value
        self.min = min
        self.next: Optional[MinNode] = None


class MinLinkedStack(LinkedStack[T]):
    def __init__(self) -> None:
        self.top: Optional[MinNode] = None

    def pop(self) -> T:
        assert self.top, "Stack is empty."
        curr = self.top.data
        self.top = self.top.next
        return curr
    
    def push(self, item: T):
        if self.is_empty():
            curr = MinNode(item, item)
        else:
            curr_min = self.min() if self.min() < item else item
            curr = MinNode(item, curr_min)

        curr.next = self.top
        self.top = curr

    def min(self) -> T:
        assert self.top, "Stack is empty."
        return self.top.min


def test_min_linked_stack() -> None:
    mls = MinLinkedStack()
    assert mls.is_empty()
    mls.push(10)
    assert mls.min() == 10
    mls.push(2)
    assert mls.min() == 2
    mls.push(3)
    mls.push(0)
    assert mls.peek() == mls.min()
    assert not mls.is_empty()
    assert mls.pop() == 0
    assert mls.peek() == 3
    assert mls.min() == 2


if __name__ == "__main__":
    test_stack()
    test_linked_stack()

    test_min_stack()
    test_min_stack_v2()
    test_min_linked_stack()
