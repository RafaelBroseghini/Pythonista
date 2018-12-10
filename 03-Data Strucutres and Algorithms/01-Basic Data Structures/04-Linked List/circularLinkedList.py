#!/usr/bin/env python

"""
Implementation of a Circular Linked List. 

Enqueueing and dequeing are done 
in constant time O(1) and we
do not need to worry about the
amortized case O(n) of a Python list
resizing.
"""

class Node(object):
  def __init__(self, data, next):
    self.data = data
    self.next = next

class CircularLinkedList():
  def __init__(self):
    self.tail = None
    self.size = 0

  def __len__(self):
    return self.size

  def isEmpty(self):
    return self.size == 0

  def peek(self):
    if self.isEmpty():
      raise Exception("Circular Linked List is empty.")
    return self.tail.next

  def enqueue(self, new_element):
    temp = Node(new_element, None)
    if self.isEmpty():
    # When list is empty the first element's
    # next points to itself.
      temp.next = temp
    else:
      temp.next = self.tail.next
      self.tail.next = temp

    self.tail = temp
    self.size += 1
  
  def dequeue(self):
    if self.isEmpty():
      raise Exception("Circular Linked List is already empty.")   
    former_head = self.tail.next
    self.tail.next = former_head.next
    self.size -= 1

    if self.isEmpty():
      # Removing the last node does not really happen
      # but since we decrease size, we make sure to 
      # reassign the last node to None.
      self.tail = None
    
    return former_head
  
  def rotate(self):
    if self.size > 0:
      self.tail = self.tail.next
      

def main():
  circ_linked_list = CircularLinkedList()

  circ_linked_list.enqueue("A")
  circ_linked_list.enqueue("B")
  circ_linked_list.enqueue("C")
  print("popping head", circ_linked_list.dequeue().data)
  print("popping head", circ_linked_list.dequeue().data)
  # print("popping head", circ_linked_list.dequeue().data)
  # print("popping head", circ_linked_list.dequeue())

  print("tail",circ_linked_list.tail.data)
  print("head",circ_linked_list.peek().data)
  print("size", len(circ_linked_list))

if __name__ == "__main__":
  main()

