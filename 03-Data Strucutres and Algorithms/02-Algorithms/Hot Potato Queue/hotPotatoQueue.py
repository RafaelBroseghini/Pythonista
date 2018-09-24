"""
    Program that simulates a hot potato game. 
    Each person is dequeued and enqueued simulating the pass of the 'hot potato'.
"""
from typing import List
from pythonds.basic.queue import Queue

def HotPotato(namelist: List[str], repetitions: int) -> List[str]:
    queue = Queue()
    for name in namelist:
        queue.enqueue(name)

    for rep in range(repetitions):
        person = queue.dequeue()
        queue.enqueue(person)

    return queue.dequeue()


def main():
    hotPotato = HotPotato(["Rafael","Mo","Jac","Marcos","Trento"],7)
    print(hotPotato)
    print(type(hotPotato))
if __name__ == '__main__':
    main()
