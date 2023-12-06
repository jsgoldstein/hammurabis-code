"""
Implement a queue that models groups of friends waiting in lines (eunque, dequeue, join)

enqueue: adds a list of people [Alice, Bob]
dequeue: removes a list of people from the queue
join:    (Bob, Carol) would allow Carol to join Bob in line
"""
from typing import List

class Queue:
    def __init__(self) -> None:
        self.queue = []
        self.people = {}
        self.size = 0
        self.serving = 0

    def enqueue(self, people: List[str]) -> None:
        for person in people:
            assert person not in self.people, f"{person} is in the queue already."
            self.people[person] = self.size + self.serving

        self.queue.append(people)
        self.size = self.size + 1

    def dequeue(self) -> List[str]:
        assert self.size > 0, "There are no people in the queue."

        people = self.queue.pop(0)
        for person in people:
            del self.people[person]

        self.size = self.size - 1
        self.serving = self.serving + 1

        return people

    def join(self, person_in_queue: str, person_joining_queue: str) -> None:
        assert person_in_queue in self.people, f"{person_in_queue} is not in the queue."
        assert person_joining_queue not in self.people, f"{person_joining_queue} is in the queue already."

        self.people[person_joining_queue] = self.people[person_in_queue]
        self.queue[self.people[person_joining_queue] - self.serving].append(person_joining_queue)


if __name__ == "__main__":
    q = Queue()
    q.enqueue(["Alice", "Bob"])
    q.enqueue(["Zach", "Yoni"])
    assert q.dequeue() == ["Alice", "Bob"]
    assert q.dequeue() == ["Zach", "Yoni"]

    q = Queue()
    q.enqueue(["Alice", "Bob"])
    q.enqueue(["Zach", "Yoni"])
    q.enqueue(["Nick", "Kevin"])
    q.join("Bob", "Carol")
    q.join("Nick", "Joe")
    assert q.dequeue() == ["Alice", "Bob", "Carol"]
    assert q.dequeue() == ["Zach", "Yoni"]
    assert q.dequeue() == ["Nick", "Kevin", "Joe"]

    q = Queue()
    q.enqueue(["Alice", "Bob"])
    try:
        q.enqueue(["Bob", "Alice"])
    except AssertionError:
        pass
    try:
        q.join("John", "James")
    except AssertionError:
        pass
    assert q.dequeue() == ["Alice", "Bob"]
    try:
        q.dequeue()
    except AssertionError:
        pass
