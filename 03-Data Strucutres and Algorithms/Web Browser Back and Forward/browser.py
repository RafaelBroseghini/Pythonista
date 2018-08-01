"""
Basic implementation of a Web Browser
'back' and 'forward' button operations.
"""

from pythonds.basic.stack import Stack

__author__ = "Rafael Broseghini"
__credits__ = ["Rafael Broseghini"]
__version__ = "1.0.1"
__maintainer__ = "Rafael Broseghini"
__email__ = "rafaellopesbroseghini@gmail.com"
__status__ = "Prototype"

class Browser(object):
  def __init__(self, current=None):
    self._current_url  = current
    self._backward = Stack()
    self._forward  = Stack()

  @property
  def backward(self):
    return self._backward
  
  @property
  def forward(self):
    return self._forward

  @property
  def current_url(self):
    return self._current_url

  @current_url.setter
  def current_url(self, new_url):
    self._current_url = new_url

  def check_back_and_forth(self, url):
    if url == "back" and self.backward.isEmpty():
      raise Exception("Can't go back to nowhere.")
    elif url == "forward" and self.forward.isEmpty():
      raise Exception("Can't go forward to nowhere.")
  
  def go_back(self):
    self.forward.push(self.current_url)
    previous = self.backward.pop()
    self.current_url = previous
  
  def go_forward(self):
    self.backward.push(self.current_url)
    forward = self.forward.pop()
    self.current_url = forward
